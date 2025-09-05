from flask import Blueprint, jsonify, request
import requests
import os

bp = Blueprint('api', __name__)

@bp.route('/weather')
def get_weather():
    city = request.args.get('city', 'London')
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        return jsonify({
            'error': 'OpenWeatherMap API key not configured',
            'message': 'Please set OPENWEATHER_API_KEY environment variable',
            'instructions': 'Get a free API key from https://openweathermap.org/api'
        }), 500
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            })
        else:
            return jsonify({'error': 'City not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500