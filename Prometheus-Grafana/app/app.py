from flask import Flask, Response
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

app = Flask(__name__)

_INF = float("inf")

graphs = {}
graphs['counter'] = Counter('python_request_operations_total',
                            'The total number of processed requests')
graphs['histogram'] = Histogram('python_request_duration_seconds',
                                'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))


@app.get('/')
async def index():
    start = time.time()
    time.sleep(0.5)
    graphs['counter'].inc()
    end = time.time()

    graphs['histogram'].observe(end - start)
    return 'Hello World!'


@app.get('/metrics')
async def metrics():
    response = []
    for name, graph in graphs.items():
        response.append(prometheus_client.generate_latest(graph))
    return Response(response, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
