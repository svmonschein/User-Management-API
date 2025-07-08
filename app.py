from flask import Flask, request # to import the class Flask from the module flask
from db import init_db, add_user, get_all_users
import json


app = Flask(__name__)   # create an object app
init_db()

@app.route("/users", methods=["GET","POST"]) 
def handle_users():
    if request.method == "GET":
        return get_all_users(), 200
    
    if request.method == "POST":
        jsonString = request.get_json()
        userJson = json.loads(jsonString) 
        add_user(userJson)
        return json.dumps({"message":"user created"}), 201   
    
