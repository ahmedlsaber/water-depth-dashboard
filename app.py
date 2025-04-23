from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)
readings = []

@app.route('/')
def index():
    # This will render index.html from the templates folder
    return render_template('index.html')

@app.route('/api/depth', methods=['POST'])
def add_reading():
    data = request.json
    depth = data.get('depth')
    sensor = data.get('sensor')  # must be 'edge' or 'middle'
    if depth is None or sensor not in ['edge', 'middle']:
        return jsonify({'error': 'Invalid data'}), 400
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    readings.append({'depth': depth, 'sensor': sensor, 'timestamp': timestamp})
    return jsonify({'message': 'Reading added'}), 201

@app.route('/api/readings')
def get_readings():
    return jsonify(readings)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
