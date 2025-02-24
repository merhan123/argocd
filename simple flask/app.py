from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test_route():
    return "Hello from /test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
