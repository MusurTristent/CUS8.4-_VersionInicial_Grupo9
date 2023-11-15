from utils.ma import ma
from models.propietario import Propietario

class PropietarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Propietario
        fields = ('id_propietario', 'id_persona', 'id_casa', 'pago_responsable')

propietario_schema = PropietarioSchema()
propietarios_schema = PropietarioSchema(many=True)
