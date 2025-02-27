from flask import Flask, Response, jsonify
from flask_cors import CORS
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# ✅ Allow frontend to access backend
CORS(app, resources={r"/*": {"origins": "*"}})

# Prometheus Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/test', methods=['GET', 'OPTIONS'])
def test():
    REQUEST_COUNT.labels(method='GET', endpoint='/test').inc()
    return jsonify({"message": "Hello from backend"}), 200

@app.route('/metrics')
def metrics():
    response = Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
    response.headers["Access-Control-Allow-Origin"] = "*"  # ✅ Allow Prometheus scraping
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"  # ✅ Allow all origins
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
