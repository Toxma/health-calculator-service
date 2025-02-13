from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    """API endpoint to calculate BMI."""
    data = request.get_json()

    if not data or 'height' not in data or 'weight' not in data:
        return jsonify({'error': 'Missing height or weight'}), 400

    try:
        height = float(data['height'])
        weight = float(data['weight'])
        bmi_value = calculate_bmi(height, weight)
        return jsonify({'bmi': bmi_value})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/bmr', methods=['POST'])
def bmr():
    """API endpoint to calculate BMR."""
    data = request.get_json()

    required_keys = {'height', 'weight', 'age', 'gender'}
    if not data or not required_keys.issubset(data):
        return jsonify({'error': 'Missing height, weight, age, or gender'}), 400

    try:
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender']
        bmr_value = calculate_bmr(height, weight, age, gender)
        return jsonify({'bmr': bmr_value})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
