from flask import Flask, render_template_string
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# HTML template that will display the pod name
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pod Info</title>
</head>
<body>
    <h1>Flask Application</h1>
    <p>This request was processed by pod: <strong>{{ pod_name }}</strong></p>
</body>
</html>
"""

@app.route('/test')
def index():
    # Get the pod name from the environment variable
    pod_name = os.getenv("HOSTNAME", "unknown-pod")
    return render_template_string(html_template, pod_name=pod_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
