from flask import Flask, jsonify
import psutil
from routes.healthz import health_bp
from routes.ping import ping_bp

app = Flask(__name__)
app.register_blueprint(health_bp)
app.register_blueprint(ping_bp)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
