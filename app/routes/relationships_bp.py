from flask import Blueprint
from app.controllers.RelationshipsController import userPostRelation, pageTagRelation

relationships_bp = Blueprint('relationships_bp', __name__)

relationships_bp.route("/userpost", methods=["GET", "POST"]) (userPostRelation)
relationships_bp.route("/pagetag", methods=["GET", "POST"]) (pageTagRelation)