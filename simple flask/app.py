from flask import Flask, Response
from prometheus_client import generate_latest, CollectorRegistry, Counter

app = Flask(__name__)

# Create a Prometheus registry
registry = CollectorRegistry()
REQUEST_COUNT = Counter('flask_app_requests', 'Total HTTP Requests', registry=registry)

@app.route('/test')
def test_route():
    REQUEST_COUNT.inc()  # Increase counter when this route is hit
    return "Hello from /test"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(registry), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Use port 5000 instead of 80 (to avoid conflicts)
