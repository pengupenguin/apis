#same setup, install necessary apps

#2nd: create an environment
$ py3 -m venv <name of the environment>

#3rd: Activate the environment
$ path\Scripts\activate.bat


#4th: install flask and otherdependencies
$ pip3 install Flask
$ pip3  install <dependencies>

#5th:Create a requimrenet.txt
$ pip3 freeze > requirements.txt



#6th Test the Development environment
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'
    
#6th.2: Setthe FLASK_APP environment variable
#Note: different syntax for windows and linuz/Mac
$ setx FLASK_APP "name_file.py"
$ set FLASK_ENV=development

#7th:run
$ flask run

#if test message was resturn successgully, then the setup is okay now
# connec to a database with an object relational mapper by defining all the things stored in DB as models. To do that create a Class

#8th: Creatting a class/model
#read the documentation regarding this


#9thimport the db variable by invoking the flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy


#10th:Configure the database(creating a database by sqllite called data.db in the same drectory)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
db = SCLAlchemy(app/<variale where flask is stored>)

#11th: set the database with a table andto do that, use the python terminal.
#stop the server and open the python terminal
$ python
>>>> from filename import db

#12th: Creating the tbales
>>> db.create_all()


