from flask import Flask, jsonify, request, Response
import pymongo
import certifi
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

from models.mesas import Mesas
from models.partidos import Partidos
from models.candidatos import Candidatos
from models.resultados import Resultados

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Mind:Mindiola97_@cluster0.ul2xebu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

baseDatos = client["DB-Votaciones"] 
# print(baseDatos.list_collection_names())

@app.route('/')
def home():
    return jsonify({"mensaje": "APP Votación"})
    #return render_template('index.html')


# ------------- MESAS ----------------------
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
        baseDatos.mesas.update_one({"_id": ObjectId(id)}, {'$set' : 
                                    {'mesa' : mesa, 'cedulas_inscritas' : cedulas_inscritas}})
        response = jsonify({'message' : 'Mesa ' + id + ' actualizada correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar una mesa por su id.
@app.route('/mesas/delete/<id>', methods=['DELETE'])
def deleteMesa(id):
    baseDatos.mesas.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Mesa '+ id +' borrada correctamente'})


# ------------- PARTIDOS ----------------------
# Metods: POST
# Opcion para agregar partidos a la base de datos.
@app.route('/partidos', methods=['POST'])
def addPartido():
    nombrePartido = request.json['nombrePartido']
    lema = request.json['lema']

    if nombrePartido and lema :
        partidoNew = Partidos(nombrePartido,lema)
        baseDatos.partidos.insert_one(partidoNew.toDBCollection())
        response = jsonify({
            "nombrePartido": nombrePartido,
            "lema": lema
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todos los partidos registrados.
@app.route('/partidos', methods=['GET'])
def getPartidos():
    partidos = baseDatos.partidos.find()
    response = json_util.dumps(partidos)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de un partido registrado por su id.
@app.route('/partidos/<id>', methods=['GET'])
def getPartido(id):
    partido = baseDatos.partidos.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(partido)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de un partido por su id.
@app.route('/partidos/update/<id>', methods=['PUT'])
def updatePartido(id):
    nombrePartido = request.json['nombrePartido']
    lema = request.json['lema']

    if nombrePartido and lema:
        baseDatos.partidos.update_one({"_id": ObjectId(id)}, {'$set' : 
                                    {'nombrePartido' : nombrePartido, 'lema' : lema}})
        response = jsonify({'message' : 'Partido ' + id + ' actualizado correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar un partido por su id.
@app.route('/partidos/delete/<id>', methods=['DELETE'])
def deletePart(id):
    baseDatos.partidos.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Partido '+ id +' borrado correctamente'})


# ------------- CANDIDATOS ----------------------
# Metods: POST
# Opcion para agregar candidatos a la base de datos.
@app.route('/candidatos', methods=['POST'])
def addCandidato():
    numero = request.json['numero']
    cedula = request.json['cedula']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    partido = request.json['partido']

    if numero and cedula and nombre and apellido and partido:
        candidatoNew = Candidatos(numero, cedula, nombre, apellido, partido)
        baseDatos.candidatos.insert_one(candidatoNew.toDBCollection())
        response = jsonify({
            "numero": numero,
            "cedula,": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "partido": partido
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todos los candidatos registrados.
@app.route('/candidatos', methods=['GET'])
def getCandidatos():
    candidatos = baseDatos.candidatos.find()
    response = json_util.dumps(candidatos)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de un candidato registrado por su id.
@app.route('/candidatos/<id>', methods=['GET'])
def getCandidato(id):
    candidato = baseDatos.candidatos.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(candidato)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de un candidato por su id.
@app.route('/candidatos/update/<id>', methods=['PUT'])
def updateCandidato(id):
    numero = request.json['numero']
    cedula = request.json['cedula']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    partido = request.json['partido']

    if numero and cedula and nombre and apellido and partido:
        baseDatos.candidatos.update_one({"_id": ObjectId(id)}, {'$set' : 
                                        {'numero' : numero, 'cedula' : cedula, 'nombre' : nombre, 
                                        'apellido' : apellido, 'partido' : partido}})
        response = jsonify({'message' : 'Candidato ' + id + ' actualizado correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar un candidato por su id.
@app.route('/candidatos/delete/<id>', methods=['DELETE'])
def deleteCand(id):
    baseDatos.candidatos.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Candidato '+ id +' borrado correctamente'})


# ------------- RESULTADOS ----------------------
# Metods: POST
# Opcion para agregar resultados a la base de datos.
@app.route('/resultados', methods=['POST'])
def addResultado():
    mesa = request.json['mesa']
    numeroCandidato = request.json['numeroCandidato']
    partido = request.json['partido']
    votos = request.json['votos']

    if mesa and numeroCandidato and partido and votos:
        resultadoNew = Resultados(mesa, numeroCandidato, partido, votos)
        baseDatos.resultados.insert_one(resultadoNew.toDBCollection())
        response = jsonify({
            "mesa": mesa,
            "numeroCandidato": numeroCandidato,
            "partido": partido,
            "votos": votos
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todos los partidos registradas.
@app.route('/resultados', methods=['GET'])
def getResultados():
    resultados = baseDatos.resultados.find()
    response = json_util.dumps(resultados)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de un partido registrado por su id.
@app.route('/resultados/<id>', methods=['GET'])
def getResultado(id):
    resultado = baseDatos.resultados.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(resultado)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de un resultado por su id.
@app.route('/resultados/update/<id>', methods=['PUT'])
def updateResultado(id):
    mesa = request.json['mesa']
    numeroCandidato = request.json['numeroCandidato']
    partido = request.json['partido']
    votos = request.json['votos']

    if mesa and numeroCandidato and partido and votos:
        baseDatos.resultados.update_one({"_id": ObjectId(id)}, {'$set' : 
                                        {'mesa' : mesa, 'numeroCandidato' : numeroCandidato, 'partido' : partido, 
                                        'votos' : votos}})
        response = jsonify({'message' : 'Resultado ' + id + ' actualizado correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar un resultado por su id.
@app.route('/resultados/delete/<id>', methods=['DELETE'])
def deleteRes(id):
    baseDatos.resultados.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Resultado '+ id +' borrado correctamente'})


#----------------ERROR-----------------------
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