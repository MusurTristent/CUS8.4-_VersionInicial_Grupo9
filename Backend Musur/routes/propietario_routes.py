from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.propietario import Propietario
from schemas.propietario_schema import propietario_schema, propietarios_schema

propietario_routes = Blueprint("propietario_routes", __name__)

@propietario_routes.route('/propietario', methods=['POST'])
def create_Propietario():
    id_persona = request.json.get('id_persona')
    id_casa = request.json.get('id_casa')
    pago_responsable = request.json.get('pago_responsable')

    new_propietario = Propietario(id_persona, id_casa, pago_responsable)

    db.session.add(new_propietario)
    db.session.commit()

    result = propietario_schema.dump(new_propietario)

    data = {
        'message': 'Nuevo Propietario creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@propietario_routes.route('/propietario', methods=['GET'])
def get_Propietarios():
    all_propietarios = Propietario.query.all()
    result = propietarios_schema.dump(all_propietarios)

    data = {
        'message': 'Todos los Propietarios',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@propietario_routes.route('/propietario/<int:id>', methods=['GET'])
def get_Propietario(id):
    propietario = Propietario.query.get(id)

    if not propietario:
        data = {
            'message': 'Propietario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = propietario_schema.dump(propietario)

    data = {
        'message': 'Propietario encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@propietario_routes.route('/propietario/<int:id>', methods=['PUT'])
def update_Propietario(id):
    propietario = Propietario.query.get(id)

    if not propietario:
        data = {
            'message': 'Propietario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_persona = request.json.get('id_persona')
    id_casa = request.json.get('id_casa')
    pago_responsable = request.json.get('pago_responsable')

    propietario.id_persona = id_persona
    propietario.id_casa = id_casa
    propietario.pago_responsable = pago_responsable

    db.session.commit()

    result = propietario_schema.dump(propietario)

    data = {
        'message': 'Propietario actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@propietario_routes.route('/propietario/<int:id>', methods=['DELETE'])
def delete_Propietario(id):
    propietario = Propietario.query.get(id)

    if not propietario:
        data = {
            'message': 'Propietario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(propietario)
    db.session.commit()

    data
