# Se importa flask desde la libreria
from flask import Flask, request, jsonify, Response
# Se importa pymongo que sirve para la conexion con mogoDB
from flask_pymongo import PyMongo
# Se importa libreria que permite poder encriptar la contraseña
from werkzeug.security import generate_password_hash, check_password_hash
# Se importa la libreria de bson
# Bson es el tipo de dato que ocupa mongo para pode almacenar datos
from bson import json_util
# Creamos una instancia del Framework Flask llamado "app"
app = Flask(__name__)

# Se configura la conexion a localhost
app.config['MONGO_URI'] = 'mongodb://localhost/pymonAccount'

# Se crea una variable "mongo" que contiene Pymongo envolviendo la app
mongo = PyMongo(app)

# ======================= ROUTES ================================


# Ruta para la creacion de nuevos elementos


@app.route('/users', methods=['POST'])
def create_user():  # Funcion de la ruta
    # variables que contienen los datos que se le enviaran al backend
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    age = request.json['age']
    student = request.json['student']

    # Condicion que permite poder verificar que todos los datos se reciban
    if username and password and email and age and student:
        # Se encripta la contraseña del usuario
        hashed_password = generate_password_hash(password)
        # La variable id es el resultado de la inserccion de los datos
        id = mongo.db.users.insert(
            {'username': username, 'password': hashed_password,
             'email': email, 'age': age, 'student': student}
        )
        response = {
            'id': str(id),
            'username': username,
            'password': hashed_password,
            'email': email,
            'age': age,
            'student': student
        }
        return response
    else:
        return notfound()


@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')
# Manejador de error


@app.errorhandler(404)
def notfound(error=None):
    # La variable response contiene el mensaje de error
    response = jsonify({
        'message': 'Recurso no encontrado' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


# Se crea la condicional la cual permite poder runear el programa
if __name__ == "__main__":
    app.run(debug=True)
