#windows: 1st:How to create a virtual env
#$ are terminal codes
$ py -3 -m venv venv

#2nd: Change the interpreter into the Scripts\python.exe

#3rd:terminal should also be using the venv
$venv\Scripts\activate.bat

#4th step using fastapi
#installing fastapi
$ pip installfastapi[all]

#to see all the dependencies installed

$ pip freeze

#import fastapi in vscodde
from fastapi import FastAPI

app = FastAPI()

#pathoperation/route
@app.get("/") #decorator/act to like an api/to create an endpoint of an api
async def root(): #a function/async=to do asynchronously
    return {"message": "Hello World"}

#start the webserver
$ uvicorn my_first_api:app

#any changes,restart the server through terminal or
uvicorn my_first_api:app --reload
  
  
