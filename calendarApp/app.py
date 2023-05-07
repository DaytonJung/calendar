from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tempsecret'

#an array to store tasks - THIS WILL BE REPLACED BY DATABASE
tasks = ["learn flask", "set up venv", "use a database"]

#class to manage the manual task input
class TaskForm(FlaskForm):
    task = StringField("Input a task")
    submit = SubmitField('Add task')

#handles any request to the home page
@app.route('/', methods=["GET", "POST"])
def index():

    #if a POST request has a 'task' attribute append it to the tasks array
    if 'task' in request.form:
        tasks.append(request.form['task'])

    #rendering the corresponding html template image
    #taskForm=TaskForm -> 'veriable name in the html'='Class/object from this code' <--- note for learning
    return render_template('index.html', tasks=tasks, taskForm=TaskForm())
