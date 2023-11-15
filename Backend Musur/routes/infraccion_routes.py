from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.infraccion import Infraccion
from schemas.infraccion_schema import infraccion_schema, infracciones_schema

infraccion_routes = Blueprint("infraccion_routes", __name__)

@infraccion_routes.route('/infraccion', methods=['POST'])
def create_Infraccion():
    codigo = request.json.get('codigo')
    descripcion = request.json.get('descripcion')
    importe = request.json.get('importe')
    fecha_registro = request.json.get('fecha_registro')
    fecha_autorizacion = request.json.get('fecha_autorizacion')

    new_infraccion = Infraccion(codigo, descripcion, importe, fecha_registro, fecha_autorizacion)

    db.session.add(new_infraccion)
    db.session.commit()

    result = infraccion_schema.dump(new_infraccion)

    data = {
        'message': 'Nueva Infraccion creada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@infraccion_routes.route('/infraccion', methods=['GET'])
def get_Infracciones():
    all_infracciones = Infraccion.query.all()
    result = infracciones_schema.dump(all_infracciones)

    data = {
        'message': 'Todas las Infracciones',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@infraccion_routes.route('/infraccion/<int:id>', methods=['GET'])
def get_Infraccion(id):
    infraccion = Infraccion.query.get(id)

    if not infraccion:
        data = {
            'message': 'Infraccion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = infraccion_schema.dump(infraccion)

    data = {
        'message': 'Infraccion encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@infraccion_routes.route('/infraccion/<int:id>', methods=['PUT'])
def update_Infraccion(id):
    infraccion = Infraccion.query.get(id)

    if not infraccion:
        data = {
            'message': 'Infraccion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    codigo = request.json.get('codigo')
    descripcion = request.json.get('descripcion')
    importe = request.json.get('importe')
    fecha_registro = request.json.get('fecha_registro')
    fecha_autorizacion = request.json.get('fecha_autorizacion')

    infraccion.codigo = codigo
    infraccion.descripcion = descripcion
    infraccion.importe = importe
    infraccion.fecha_registro = fecha_registro
    infraccion.fecha_autorizacion = fecha_autorizacion


    db.session.commit()

    result = infraccion_schema.dump(infraccion)

    data = {
        'message': 'Infraccion actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@infraccion_routes.route('/infraccion/<int:id>', methods=['DELETE'])
def delete_Infraccion(id):
    infraccion = Infraccion.query.get(id)

    if not infraccion:
        data = {
            'message': 'Infraccion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(infraccion)
    db.session.commit()

    data = {
        'message': 'Infraccion eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)