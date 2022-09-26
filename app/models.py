from datetime import datetime
#importamos la base de datos definida en app
from app import db

#Un modelo de usuario con id autoincrementando
#un string username de hasta 64 caracteres
#un string email de hasta 120 caracteres
#un stirng password de hasta 128 caracteres
#este modelo corresponde a la tabla con las siguientes columnas
#y algunos ejemplos de filas
#  id | username  |       email          | password
#  1  | jpazos    | jpazos@utec.edu.pe   | jpazos123
#  2  | ctorres   | ctorres@utec.edu.pe  | contrasena123
# ...
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    age = db.Column(db.Integer)
    #relacion con la tabla post, escrita como una clase
    #esto no es una columna de la tabla, solo permite a flask-sqlalchemy 
    #hacer los queries automaticamente
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    #permite imprimir el objeto usuario y mostrar datos
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #esta columna tiene relacion de foreign key con la columna id de user, escrita como SQL
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(2))
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return '<Review {} {}>'.format(self.rating, self.description)


class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(8), index=True, unique=True)
    nombre = db.Column(db.String(20), index=True, unique=True)
    apellido = db.Column(db.String(20))

    def __repr__(self):
        return '<Estudiante {} {}>'.format(self.nombre, self.apellido)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __repr__(self):
        return '<Usuario {} {}>'.format(self.username, self.email)


association_table = db.Table('association',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=association_table, backref='pages')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)