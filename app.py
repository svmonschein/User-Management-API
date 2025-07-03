from flask import Flask, request # to import the class Flask from the module flask
from db import init_db, add_user, get_all_users
import json


app = Flask(__name__)   # create an object app
# init_db()

@app.route("/users", methods=["GET","POST"]) 
def handle_users():
    if request.method == "GET":
        return get_all_users(), 200
    
    if request.method == "POST":
        userJson = request.get_json()
        print(userJson)
        user = json.loads(userJson) 
        print(user)
        # add_user(user)
        return 201   
    
