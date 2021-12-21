from enum import unique
from database import db, event, DDL


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages

    def __repr__(self) -> str:
        return f'<Book={self.title} pages={self.pages}>'

    def json(self) -> dict:
        return {
            'title': self.title,
            'pages': self.pages
        }


@classmethod
def find_by_id(cls, _id: int) -> BookModel:
    return cls.query.filter_by(id=_id).first()


@classmethod
def find_by_title(cls, title: str) -> BookModel:
    return cls.query.filter_by(title=title).first()


@classmethod
def find_all(cls) -> BookModel:
    return cls.query.all()


def save_to_db(self) -> None:
    db.session.add(self)
    db.session.commit()


def delete_from_db(self) -> None:
    db.session.delete(self)
    db.session.commit()


event.listen(
    BookModel.__table__,
    'after_create',
    DDL(f"select create_hypertable({BookModel.__tablename__}, 'time');")
)
