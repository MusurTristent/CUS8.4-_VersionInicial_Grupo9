from utils.db import db

class Propietario(db.Model):
    __tablename__ = "propietario"

    id_propietario = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey("persona.id_persona"))
    id_casa = db.Column(db.Integer, db.ForeignKey("casa.id_casa"))
    pago_responsable = db.Column(db.Boolean)

    def __init__ (self, id_persona, id_casa, pago_responsable):
        self.id_persona = id_persona
        self.id_casa = id_casa
        self.pago_responsable = pago_responsable