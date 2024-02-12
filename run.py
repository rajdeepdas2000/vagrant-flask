from flask import Flask, jsonify
import psutil
# from health.routes.health import health_bp
# from ping.routes.ping import ping_bp

app = Flask(__name__)
# app.register_blueprint(health_bp)
# app.register_blueprint(ping_bp)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@app.route('/healthz', methods=['GET'])
def healthz():
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    response = {
        'cpu_usage': cpu_usage,
        'memory': {
            'total': memory_info.total / (1024 * 1024),
            'used': memory_info.used / (1024 * 1024),
            'free': memory_info.free / (1024 * 1024),
            'percent': memory_info.percent
        },
        'disk_space': {
            'total': disk_info.total / (1024 * 1024),
            'used': disk_info.used / (1024 * 1024),
            'free': disk_info.free / (1024 * 1024),
            'percent': disk_info.percent
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
