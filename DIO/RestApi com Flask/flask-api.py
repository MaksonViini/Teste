from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Ola Mundo'

@app.route('/quadrado', methods=['GET'])
def calcula():
    return 5 ** 6

if __name__ == '__main__':
    app.run(debug=True)
