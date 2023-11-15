from utils.db import db

class CasaInfraccion(db.Model):
    __tablename__ = "casa_infraccion"

    id_casa_infraccion = db.Column(db.Integer, primary_key=True)
    id_infraccion = db.Column(db.Integer, db.ForeignKey("infraccion.id_infraccion"))
    id_gasto = db.Column(db.Integer, db.ForeignKey("gasto.id_gasto"))
    periodo = db.Column(db.String(255))
    fecha_infraccion = db.Column(db.Date)
    importe = db.Column(db.Numeric(6,2))

    def __init__ (self, id_infraccion, id_gasto, periodo, fecha_infraccion, importe):
        self.id_infraccion = id_infraccion
        self.id_gasto = id_gasto
        self.periodo = periodo
        self.fecha_infraccion = fecha_infraccion
        self.importe = importe
