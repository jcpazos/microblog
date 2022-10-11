from flask import Blueprint

from app.controllers.LoginController import login, register, delete, loginAsync

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (login)
login_bp.route("/async", methods=["GET", "POST"]) (loginAsync)
login_bp.route("/register", methods=["POST"]) (register)
login_bp.route("/delete", methods=["POST"]) (delete)
