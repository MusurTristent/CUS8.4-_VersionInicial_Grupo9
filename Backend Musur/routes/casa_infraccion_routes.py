from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.casa_infraccion import CasaInfraccion
from schemas.casa_infraccion_schema import casa_infraccion_schema, casa_infracciones_schema

casa_infraccion_routes = Blueprint("casa_infraccion_routes", __name__)

@casa_infraccion_routes.route('/casa_infraccion', methods=['POST'])
def create_CasaInfraccion():
    id_infraccion = request.json.get('id_infraccion')
    id_gasto = request.json.get('id_gasto')
    periodo = request.json.get('periodo')
    fecha_infraccion = request.json.get('fecha_infraccion')
    importe = request.json.get('importe')

    new_casa_infraccion = CasaInfraccion(id_infraccion, id_gasto, periodo, fecha_infraccion, importe)

    db.session.add(new_casa_infraccion)
    db.session.commit()

    result = casa_infraccion_schema.dump(new_casa_infraccion)

    data = {
        'message': 'Nueva Casa Infraccion creada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@casa_infraccion_routes.route('/casa_infraccion', methods=['GET'])
def get_CasaInfracciones():
    all_casa_infracciones = CasaInfraccion.query.all()
    result = casa_infracciones_schema.dump(all_casa_infracciones)

    data = {
        'message': 'Todas las Casa Infracciones',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@casa_infraccion_routes.route('/casa_infraccion/<int:id>', methods=['GET'])
def get_CasaInfraccion(id):
    casa_infraccion = CasaInfraccion.query.get(id)

    if not casa_infraccion:
        data = {
            'message': 'Casa Infraccion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = casa_infraccion_schema.dump(casa_infraccion)

    data = {
        'message': 'Casa Infraccion encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@casa_infraccion_routes.route('/casa_infraccion/<int:id>', methods=['PUT'])
def update_CasaInfraccion(id):
    casa_infraccion = CasaInfraccion.query.get(id)

    if not casa_infraccion:
        data = {
            'message': 'Casa Infraccion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_infraccion = request.json.get('id_infraccion')
    id_gasto = request.json.get('id_gasto')
    periodo = request.json.get('periodo')
    fecha_infraccion = request.json.get('fecha_infraccion')
    importe = request.json.get('importe')

    casa_infraccion.id_infraccion = id_infraccion
    casa_infraccion.id_gasto = id_gasto
    casa_infraccion.periodo = periodo
    casa_infraccion.fecha_infraccion = fecha_infraccion
    casa_infraccion.importe = importe

    db.session.commit()

    result = casa_infraccion_schema.dump(casa_infraccion)

    data = {
        'message': 'Casa Infraccion actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@casa_infraccion_routes.route('/casa_infraccion/<int:id>', methods=['DELETE'])
def delete_CasaInfraccion(id):
    casa_infraccion = CasaInfraccion.query.get(id)

    if not casa_infraccion:
        data = {
            'message': 'Casa Infraccion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(casa_infraccion)
    db.session.commit()

    data = {
        'message': 'Casa Infraccion eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)