from mashmallow import ma
from models.timescale import BookPrice


class BookPriceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookPrice
        load_instance = True
