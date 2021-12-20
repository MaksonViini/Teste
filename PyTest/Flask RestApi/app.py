from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    'id': 1,
    'value': 10
}


@app.route('/', methods=['GET'])
def index():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
