import mysql.connector
from datetime import date

class TaskDatabase:
    #Initializes class
    def __init__(self, host, username, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()
        #create a task table if it does not exist when the fucntion is called
        self._createTable()

    #creates a table of interest
    def _createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST Task (
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(255) NOT NULL,
                description VARCHAR(1000) NOT NULL,
                status ENUM("ToDo", "Blocked", "In Progress", "Done", "Recurring", "Hidden"),
                priority SMALLINT NOT NULL,
                start DATETIME NOT NULL,
                end DATETIME NOT NULL
            )
        """)

    def addTask(self, title, description, status, priority, start, end):
        sql = "INSERT INTO Task (title, description, status, priority, start, end) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (title, description, status, priority, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S'))
        self.cursor.execute(sql, values)
        self.db.commit()

    def getTask(self, id):
        sql = "SELECT * FROM Task WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def updateTask(self, id, field, value):
        sql = f"UPDATE Task SET {field} = %s WHERE id = %s"
        values = (value, id)
        self.cursor.execute(sql, values)
        self.db.commit()

    def deleteTask(self, id):
        sql = "DELETE FROM Task WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.db.commit()

    def closeConnection(self):
        self.cursor.close()
        self.db.close()

#Database is not being recognized- could be because we are in a vertual envrionemnt 
#code above should be effective - old DB is kept just incase though its infromation was not persisting either most likely for the same reason
db = TaskDatabase(host="127.0.0.1", username="root", password="Leaf-Grow-Cold", database="TaskDatabase")

db.add_task(
    title="Write a class",
    description="Write a class that creates a database with a table called Task",
    status="In Progress",
    priority=1,
    start_date="2023-05-07",
    end_date="2023-05-14"
)

task = db.get_task(1)
print(task)  # prints the task with ID 1

db.update_task(1, "status", "Complete")
