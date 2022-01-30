from monitoring import Monitoring
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge

graphs = {'counter': 0, 'counter1': 0}


def teste1():
    func = Monitoring(graphs)
    func.get_counter('python_request_operations_total',
                    'The total number of processed requests')
    func.Counter('counter')
    func.Counter('counter1')
    
    print(func.graphs.items())



teste1()


# _INF = float("inf")


# func.get_histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', (1, 2, 5, 6, 10))

# func1.Counter('counter')
# func.Histogram('histogram')


# func.inc('counter')

# print(func.metrics())
# print(func1.graphs.items())


# graphs = {}

# counter = Counter('python_request_operations_total', 'The total number of processed requests')

# graphs['counter_index'] = counter
# graphs['counter_time'] = counter

# print(graphs.items())

# index.inc()

# Monitoring('counter').Counter('python_request_operations_total', 'The total number of processed requests')
