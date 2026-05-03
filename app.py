from flask import Flask, render_template, request, jsonify
import math
import requests
from functools import lru_cache

app = Flask(__name__)

# Get country from coordinates

@lru_cache(maxsize=100)
def get_country(lat, lng):
    try:
        url = "https://nominatim.openstreetmap.org/reverse"

        params = {
            "lat": lat,
            "lon": lng,
            "format": "json"
        }

        headers = {
            "User-Agent": "nearby-places-app"
        }

        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()

        return data.get("address", {}).get("country", "")

    except Exception as e:
        print("Country fetch error:", e)
        return ""



#  Sample places data

places_data = [
    # 📍 Nellore
    {"name": "Nellore Tank", "lat": 14.4426, "lng": 79.9865, "country": "India", "city": "Nellore"},
    {"name": "Mypadu Beach", "lat": 14.0250, "lng": 80.1710, "country": "India", "city": "Nellore"},
    {"name": "Nellore Park", "lat": 14.4505, "lng": 79.9900, "country": "India", "city": "Nellore"},
    {"name": "Mini Zoo Park", "lat": 14.4530, "lng": 79.9860, "country": "India", "city": "Nellore"},

    # 🛕 India
    {"name": "Ranganayaka Temple", "lat": 14.8788, "lng": 79.2979, "country": "India", "city": "Nellore"},
    {"name": "Tirupati Balaji Temple", "lat": 13.6833, "lng": 79.3475, "country": "India", "city": "Tirupati"},
    {"name": "Taj Mahal", "lat": 27.1751, "lng": 78.0421, "country": "India", "city": "Agra"},
    {"name": "Charminar", "lat": 17.3616, "lng": 78.4747, "country": "India", "city": "Hyderabad"},
    {"name": "India Gate", "lat": 28.6129, "lng": 77.2295, "country": "India", "city": "Delhi"},
    {"name": "Gateway of India", "lat": 18.9220, "lng": 72.8347, "country": "India", "city": "Mumbai"},

    # 🌍 World
    {"name": "Eiffel Tower", "lat": 48.8584, "lng": 2.2945, "country": "France", "city": "Paris"},
    {"name": "Statue of Liberty", "lat": 40.6892, "lng": -74.0445, "country": "USA", "city": "New York"},
    {"name": "Sydney Opera House", "lat": -33.8568, "lng": 151.2153, "country": "Australia", "city": "Sydney"},
    {"name": "Southern Cross Station", "lat": -37.8183, "lng": 144.9525, "country": "Australia", "city": "Melbourne"},

    # 🌆 More landmarks
    {"name": "Burj Khalifa", "lat": 25.1972, "lng": 55.2744, "country": "UAE", "city": "Dubai"},
    {"name": "Big Ben", "lat": 51.5007, "lng": -0.1246, "country": "UK", "city": "London"},
    {"name": "Great Wall of China", "lat": 40.4319, "lng": 116.5704, "country": "China", "city": "Beijing"},

    # 🏞️ Nature
    {"name": "Grand Canyon", "lat": 36.1069, "lng": -112.1129, "country": "USA", "city": "Arizona"},
    {"name": "Niagara Falls", "lat": 43.0962, "lng": -79.0377, "country": "Canada", "city": "Ontario"}
]


# Distance calculation

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c



# Home page

@app.route('/')
def home():
    return render_template('index.html')



# Get nearby places

@app.route('/get_places', methods=['POST'])
def get_places():
    try:
        data = request.get_json()

        user_lat = float(data['lat'])
        user_lng = float(data['lng'])

        max_distance = float(data.get("distance", 10))
        country_filter = data.get("country", "")

        # optional auto-detect
        if not country_filter:
            user_country = get_country(user_lat, user_lng)
        else:
            user_country = country_filter

        nearby_places = []

        for place in places_data:

            # country filtering
            if user_country and place["country"] != user_country:
                continue

            distance = calculate_distance(
                user_lat, user_lng,
                place["lat"], place["lng"]
            )

            if distance <= max_distance:
                nearby_places.append({
                    "name": place["name"],
                    "distance": round(distance, 2),
                    "lat": place["lat"],
                    "lng": place["lng"]
                })

        # ✅ sort nearest first
        nearby_places.sort(key=lambda x: x["distance"])

        return jsonify(nearby_places)

    except Exception as e:
        print("ERROR:", e)
        return jsonify([])



# Run server

if __name__ == '__main__':
    app.run(debug=True)