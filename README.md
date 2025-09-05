# Weather Web App

A Flask-based web application that provides weather information using the OpenWeatherMap API.

## Features

- Real-time weather data for any city
- User authentication system
- Interactive maps integration
- Responsive web interface
- SQLite database for user management

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd weather_web
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Get your OpenWeatherMap API key from https://openweathermap.org/api
   - Get your Google Maps API key from https://developers.google.com/maps
   - Add your API keys to the `.env` file

5. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

- `GET /api/weather?city=<city_name>` - Get weather data for a specific city

## Environment Variables

- `OPENWEATHER_API_KEY` - Your OpenWeatherMap API key
- `GOOGLE_MAPS_API_KEY` - Your Google Maps API key
- `SECRET_KEY` - Flask secret key for sessions
- `DATABASE_URL` - Database connection string
- `JWT_SECRET_KEY` - JWT secret for authentication

## Requirements

- Python 3.7+
- Flask
- SQLAlchemy
- OpenWeatherMap API key
- Google Maps API key (optional)

## License

MIT License
