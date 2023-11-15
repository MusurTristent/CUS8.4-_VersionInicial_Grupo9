from utils.ma import ma
from models.casa_infraccion import CasaInfraccion

class CasaInfraccionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CasaInfraccion
        fields = ('id_casa_infraccion', 'id_infraccion', 'id_gasto', 'periodo', 'fecha_infraccion', 'importe')

casa_infraccion_schema = CasaInfraccionSchema()
casa_infracciones_schema = CasaInfraccionSchema(many=True)
