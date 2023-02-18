from chalice import Chalice, Rate
import logging

app = Chalice(app_name="Chalice")
app.log.setLevel(logging.DEBUG)


@app.route("/health")
def index():
    return {"Ping": "Pong"}


@app.route("/teste")
def teste_lambda_handler():
    return {"Message": "Testando o Lambda Handler com Chalice"}


@app.route("/query")
def query():
    return {"Message": "Query!", "Params": app.current_request.query_params}


@app.route("/post-router", methods=["POST"])
def post_func():
    return {"Message": "Post Method!", "Params": app.current_request.json_body}


@app.lambda_function(name="teste-function")
def my_lambda(request, context):
    return {"Message": "My lambda integration!"}


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduler(event):
    app.log.info("Scheduler Executado!")


@app.on_s3_event(bucket="teste")
def s3_event(event):
    app.log.info("Scheduler Executado a partir do Bucket!")
    app.log.info(f"{event.bucket}, {event.key}")


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
