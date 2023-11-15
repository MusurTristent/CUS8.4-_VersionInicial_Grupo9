from utils.db import db

class Infraccion(db.Model):
    __tablename__ = "infraccion"

    id_infraccion = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    importe = db.Column(db.Float)
    fecha_registro = db.Column(db.Date)
    fecha_autorizacion = db.Column(db.Date)

    def __init__ (self, codigo, descripcion, importe, fecha_registro, fecha_autorizacion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.importe = importe
        self.fecha_registro = fecha_registro
        self.fecha_autorizacion = fecha_autorizacion

