from database import db
from models.book import BookModel


class BookPrice(db.Model):
    __tablename__ = 'book_price'
    time = db.Column(db.DateTime(timezone=True),
                     nullable=False, server_default=db.func.now(), primary_key=True)
    price = db.Column(db.Float, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    def __init__(self, price: float) -> None:
        self.price = price
        self.time = db.func.now()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()