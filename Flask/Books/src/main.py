from flask_restx import Api
from mashmallow import ma
from database import db
from models.timescale import BookPrice
from controllers.book import Book, Home
# from mashmallow import ValidationError

from server.instance import server

app, api = server.app, server.api


@app.before_first_request
def create_tables():
    db.create_all()


@app.before_first_request
def create_hyper_table():
    db.engine.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")
    db.engine.execute(
        f"select create_hypertable('{BookPrice.__tablename__}', 'time');")


api.add_resource(Book, '/books/<int:id>')
api.add_resource(Home, '/home/')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
