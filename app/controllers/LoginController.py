from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import User
import requests
import json
from cryptography.hazmat.primitives import hashes

def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            return "Missing form parameter username or password"
        try:
            user = User.query.filter(User.username == username).first()
            if user == None or password != user.password:
                return "Invalid user or password"
            email = user.email
            password = bytes(password, "utf-8")
            digest = hashes.Hash(hashes.SHA256())
            digest.update(password)
            hashedPassword = str(digest.finalize())
            return redirect("/profile?username="+username+"&password="+hashedPassword+"&email="+email)
        except Exception as err:
            print(err)
            return "Error while accesing user. Try again."
    return render_template("login.html")

def register():
    print("register")
    body = request.get_json()
    print(body)
    user = User(username=body["newUsername"], password=body["newPassword"], email=body["newEmail"])
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return json.dumps({"success": False, "username": user.username, "email": user.email}) 

    return json.dumps({"success": True, "username": user.username, "email": user.email})

def delete():
    body = request.get_json()
    user = User.query.filter(User.username == body["username"]).first()

    if user == None:
        return json.dumps({"success":False})

    try:
        db.session.delete(user)
        db.session.commit()
    except:
        return json.dumps({"success":False})

    return json.dumps({"success":True, "username":user.username})

def loginAsync():
    body = request.get_json()
    print(body)
    username=body["username"] 
    password=body["password"]
    try:
        user = User.query.filter(User.username == username).first()
        if user == None or password != user.password:
            return json.dumps({"success": False})
        else:
            return json.dumps({"success": True, "username": user.username})
    except:
        return json.dumps({"success": False, "username": user.username}) 
