from utils.ma import ma
from models.casa import Casa

class CasaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Casa
        fields = ('id_casa', 'id_predio', 'id_estado', 'id_predio_mdu', 'numero', 'piso', 'area', 'participacion')

casa_schema = CasaSchema()
casas_schema = CasaSchema(many=True)
