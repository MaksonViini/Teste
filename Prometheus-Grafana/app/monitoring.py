import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
from flask import Response


class Monitoring:

    def __init__(self, graphs) -> None:
        self.graphs = graphs
        self.counter = None
        self.histogram = None

    def get_counter(self, value, description):
        self.counter = prometheus_client.Counter(value, description)
    
    def get_histogram(self, value, description, buckets):
        self.histogram = prometheus_client.Histogram(value, description, buckets=buckets)

    def Counter(self, key):
        self.graphs[key] = self.counter

    # def Summary(self, key, value):
    #     self.graphs[self.type] = Summary(key, value)

    def Histogram(self, key):
       self.graphs[key] = self.histogram

    # def Gauge(self, key, value):
    #     self.graphs[self.type] = Gauge(key, value)

    def inc(self, key):
        self.graphs[key].inc()

    def observe(self, key, value):
        self.graphs[key].observe(value)

    def items(self):
        return self.graphs.items()

    def metrics(self):
        response = [
            prometheus_client.generate_latest(graph)
            for name, graph in self.graphs.items()
        ]

        return Response(response, mimetype="text/plain")
