from flask import Flask
# from health.routes.health import health_bp
# from ping.routes.ping import ping_bp

app = Flask(__name__)
# app.register_blueprint(health_bp)
# app.register_blueprint(ping_bp)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
