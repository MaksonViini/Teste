from flask import Flask, Response
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
from time import sleep, time
from monitoring import Monitoring

app = Flask(__name__)

# _INF = float("inf")

# graphs = {}

# graphs['counter_index'] = Counter('python_request_operations_total',
#                                   'The total number of processed requests')
# graphs['counter_time'] = Counter(
#     'python_request_operations_time', 'The total time of processed requests function tt')

# graphs['histogram'] = Histogram('python_request_duration_seconds',
#   
#                               'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))

graphs = {'counter': 0}


_INF = float("inf")

monitor = Monitoring(graphs)
monitor.get_counter('python_request_operations_total',
                 'The total number of processed requests')
# monitor1.get_counter('python_request_operations_total',
#                  'The total number of processed requests')
# monitor.get_histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', (1, 2, 5, 6, 10))
monitor.Counter('counter')
monitor.Counter('counter_time')
# monitor1.Counter('counter')
# monitor.Histogram('histogram')
# monitor.Histogram('histogram1')
# monitor.Counter('python_request_operations_total', 'The total number of processed requests', 'counter_time')

@app.get('/')
async def index():

    start = time()
    sleep(0.5)
    monitor.inc('counter')
    end = time()
    # monitor.observe('histogram', end - start)
    # graphs['histogram'].observe(end - start)
    return 'Hello World!'


@app.get('/time')
async def tt():
    start = time()
    sleep(1)
    monitor.inc('counter_time')
    # graphs['counter_time'].inc()
    end = time()

    # monitor.observe('histogram1', end - start)

    return str(end - start)

@app.get('/metrics')
async def metric():
    return monitor.metrics()

# @app.get('/metrics')
# async def metrics():
#     response = []
#     for name, graph in graphs.items():
#         response.append(prometheus_client.generate_latest(graph))
#     return Response(response, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
