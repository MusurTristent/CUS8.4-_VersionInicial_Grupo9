from utils.ma import ma
from models.infraccion import Infraccion

class InfraccionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Infraccion
        fields = ('id_infraccion', 'codigo', 'descripcion', 'importe', 'fecha_registro', 'fecha_autorizacion')

infraccion_schema = InfraccionSchema()
infracciones_schema = InfraccionSchema(many=True)
