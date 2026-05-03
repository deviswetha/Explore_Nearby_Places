# Explore_Nearby_Places
🌍 Explore Nearby Places
📌 Project Description

Explore Nearby Places is a web-based application that helps users discover nearby locations such as tourist attractions, landmarks, and useful places in an interactive map interface.

The application provides a smooth, modern UI inspired by map-based platforms, allowing users to:

Search for locations
View places on an interactive map
Filter results based on country
Explore details visually with animations

This project is built using Flask (Python) for the backend and HTML, CSS, JavaScript for the frontend, along with free map services like OpenStreetMap.

🚀 Features
📍 Interactive map view (OpenStreetMap / Leaflet)
🔍 Search functionality for places
🌎 Country-based filtering
📌 Dynamic markers for locations
🎥 Support for media (images/videos)
🎨 Smooth UI animations
📱 Responsive design
🛠️ Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Map API: OpenStreetMap / Leaflet.js
Data Source: Static dataset / Open APIs (like Overpass API)
⚙️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/explore-nearby-places.git
cd explore-nearby-places
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Flask App
python app.py
5️⃣ Open in Browser

Go to:

http://127.0.0.1:5000/
🧠 How It Works
🔹 Backend (Flask)
Stores or fetches location data (latitude, longitude, country)
Provides APIs to the frontend
Handles user requests (search, filtering)
🔹 Frontend
Uses Leaflet.js to render maps
Displays markers dynamically based on backend data
Handles UI interactions (search, filters, animations)
🔹 Map Integration
OpenStreetMap tiles are used (free & no API key required)
Places are plotted using coordinates
📂 Project Structure
explore-nearby-places/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── videos/
│   └── images/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
🔮 Future Enhancements
📍 “Use My Location” feature (Geolocation API)
⭐ Ratings & reviews for places
🧭 Route navigation
📊 Category-based filtering (restaurants, parks, etc.)
☁️ Database integration (MongoDB / Firebase)
🤝 Contributing

Feel free to fork this repository and contribute by submitting a pull request.
