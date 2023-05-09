import mysql.connector
from datetime import date

#kept for learning purposes TO BE DELETED
#learning from this youtube series 
# https://www.youtube.com/watch?v=91iNR0eG8kE 


#currently is connecting to he same computer but database will be moved over to old PC
db = mysql.connector.connect(
    host="localhost",
    user="Dayton",
    passwd="root",
    database="caldatabase"
    )

calCursor = db.cursor()

#creates a new database
calCursor.execute("CREATE DATABASE IF NOT EXISTS caldatabase")

#to remove the table if it needs to be updated
#calCursor.execute("DROP TABLE Task")

#creates table
calCursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Task 
    (id int PRIMARY KEY AUTO_INCREMENT, 
    title VARCHAR(50), 
    description VARCHAR(1000), 
    status ENUM("ToDo", "Blocked", "In Progress", "Done", "Recurring", "Hidden"), 
    priority smallint UNSIGNED, 
    start datetime, 
    end datetime)
    """
    )

#exaple of an object commit into a database
#calCursor.execute("INSERT INTO Task (title, description ,status ,priority ,start ,end) VALUES (%s,%s,%s,%s,%s,%s)", ("Set Up SQL", "Set up an SQL Database", "In Progress", 2, "2023-05-07","2023-05-10"))
#db.commit()

#view the conent of the table
calCursor.execute("SELECT * FROM Task")
for x in calCursor:
    print(x)
