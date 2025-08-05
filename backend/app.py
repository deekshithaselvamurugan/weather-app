from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("WEATHER_API_KEY")

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'City not found'}), 404
    data = response.json()
    return jsonify({
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
