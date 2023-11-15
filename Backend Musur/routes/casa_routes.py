from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.casa import Casa
from schemas.casa_schema import casa_schema, casas_schema

casa_routes = Blueprint("casa_routes", __name__)

@casa_routes.route('/casa', methods=['POST'])
def create_Casa():
    id_predio = request.json.get('id_predio')
    id_estado = request.json.get('id_estado')
    id_predio_mdu = request.json.get('id_predio_mdu')
    numero = request.json.get('numero')
    piso = request.json.get('piso')
    area = request.json.get('area')
    participacion = request.json.get('participacion')

    new_casa = Casa(id_predio, id_estado, id_predio_mdu, numero, piso, area, participacion)

    db.session.add(new_casa)
    db.session.commit()

    result = casa_schema.dump(new_casa)

    data = {
        'message': 'Nueva Casa creada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@casa_routes.route('/casa', methods=['GET'])
def get_Casas():
    all_casas = Casa.query.all()
    result = casas_schema.dump(all_casas)

    data = {
        'message': 'Todas las Casas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@casa_routes.route('/casa/<int:id>', methods=['GET'])
def get_Casa(id):
    casa = Casa.query.get(id)

    if not casa:
        data = {
            'message': 'Casa no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = casa_schema.dump(casa)

    data = {
        'message': 'Casa encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@casa_routes.route('/casa/<int:id>', methods=['PUT'])
def update_Casa(id):
    casa = Casa.query.get(id)

    if not casa:
        data = {
            'message': 'Casa no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_predio = request.json.get('id_predio')
    id_estado = request.json.get('id_estado')
    id_predio_mdu = request.json.get('id_predio_mdu')
    numero = request.json.get('numero')
    piso = request.json.get('piso')
    area = request.json.get('area')
    participacion = request.json.get('participacion')

    casa.id_predio = id_predio
    casa.id_estado = id_estado
    casa.id_predio_mdu = id_predio_mdu
    casa.numero = numero
    casa.piso = piso
    casa.area = area
    casa.participacion = participacion

    db.session.commit()

    result = casa_schema.dump(casa)

    data = {
        'message': 'Casa actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@casa_routes.route('/casa/<int:id>', methods=['DELETE'])
def delete_Casa(id):
    casa = Casa.query.get(id)

    if not casa:
        data = {
            'message': 'Casa no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(casa)
    db.session.commit()

    data = {
        'message': 'Casa eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)