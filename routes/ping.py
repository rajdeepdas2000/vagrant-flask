from flask import Blueprint, jsonify

ping_bp = Blueprint('ping', __name__)

@ping_bp.route('/ping', methods=['GET'])
def ping():
    try:
        return jsonify({'Status': 'Up 👍'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
