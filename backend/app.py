from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/process": {"origins": "*"}})

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    output = f"Received: {data['input']}"  # Simple response for testing
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
