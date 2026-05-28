import os
from fastapi import FastAPI
import requests as request
from fastapi.responses import RedirectResponse
from os import getenv
app = FastAPI()


@app.get("/data")
def data():
    try:
        respone = request.get(os.getenv("SERVICE2_URL")) #fetch the url from environment variable
        data = respone.json() # Assuming Service 2 returns JSON data
    except:
        data = {"error": "Service 2 is not available"}

    return {"message": "Hello from Service 1! Version-2", "service2_data": data}

@app.get("/add")
def doc():
    return RedirectResponse(url="http://192.168.49.2:30081/docs")

@app.get("/get")
def get():
    return{"message":"Hello from Service 1"}
    