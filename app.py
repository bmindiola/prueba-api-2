from flask import Flask, jsonify, request, Response, render_template
import pymongo
import certifi
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

from models.mesas import Mesas
from models.partidos import partidos
from models.candidatos import candidatos
from models.resultados import resultados

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Mind:Mindiola97_@cluster0.ul2xebu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

baseDatos = client["DB-Votaciones"] 
print(baseDatos.list_collection_names())

@app.route('/')
def home():
    return jsonify({"mensaje": "mesas para votación"})
    #return render_template('index.html')

# Metods: POST
# Opcion para agregar mesas a la base de datos.
@app.route('/mesas', methods=['POST'])
def addMesa():
    mesa = request.json['mesa']
    cedulas_inscritas = request.json['cedulas_inscritas']

    if mesa and cedulas_inscritas :
        mesaNew = Mesas(mesa,cedulas_inscritas)
        baseDatos.mesas.insert_one(mesaNew.toDBCollection())
        response = jsonify({
            "mesa": mesa,
            "cedulas_inscritas": cedulas_inscritas
        })
        return response
    return notFound()
            

# Metods: GET
# Opcion para obtener los datos todas las mesas registradas.
@app.route('/mesas', methods=['GET'])
def getMesas():
    mesas = baseDatos.mesas.find()
    response = json_util.dumps(mesas)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de una mesa registrada por su id.
@app.route('/mesas/<id>', methods=['GET'])
def getMesa(id):
    mesa = baseDatos.mesas.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(mesa)
    return Response (response, mimetype='application/json')


# Metods: PUT
# Opcion para actualizar los datos de una mesa por su id.
@app.route('/mesas/update/<id>', methods=['PUT'])
def updateMesa(id):
    mesa = request.json['mesa']
    cedulas_inscritas = request.json['cedulas_inscritas']

    if mesa and cedulas_inscritas:
        baseDatos.mesas.update_one({"_id": ObjectId(id)}, {'$set' : {'mesa' : mesa, 'cedulas_inscritas' : cedulas_inscritas}})
        response = jsonify({'message' : 'Mesa ' + id + ' actualizada correctamente'})
        return response
    return notFound()


# Metods: DELETE
#Opción para eliminar una mesa por su id.
@app.route('/mesas/delete/<id>', methods=['DELETE'])
def delete(id):
    baseDatos.mesas.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Mesa '+ id +' borrada correctamente'})

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=9999)