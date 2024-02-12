from flask import Blueprint, jsonify
import psutil

health_bp = Blueprint('health', __name__)

@health_bp.route('/healthz', methods=['GET'])
def healthz():
    try:
        # Your code here
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

        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
