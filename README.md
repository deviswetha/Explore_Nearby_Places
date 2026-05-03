# Explore_Nearby_Places

🌍 Explore Nearby Places

📌 Project Description

Explore Nearby Places is a web-based application that helps users discover nearby locations such as tourist attractions, landmarks, and useful places in an interactive map interface.

The application provides a smooth, modern UI inspired by map-based platforms, allowing users to:

1. Search for locations
2. View places on an interactive map
3. Filter results based on country
4. Explore details visually with animations
5. This project is built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend, along with free map services like OpenStreetMap.

🚀 Features

1. Interactive map view (OpenStreetMap / Leaflet)
2. Search functionality for places
3. Country-based filtering
4. Dynamic markers for locations
5. Support for media (images/videos)
6. Smooth UI animations
7. Responsive design
8. Tech Stack

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
venv\Scripts\activate   (On Windows)
OR
source venv/bin/activate   (On Mac/Linux)

3️⃣ Install Dependencies :
 pip install -r requirements.txt

4️⃣ Run the Flask App :
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

 🔮Future Enhancements
 1. “Use My Location” feature (Geolocation API)
 2. Ratings & reviews for places
 3. Route navigation
 4. Category-based filtering (restaurants, parks, etc.)
 5.  Database integration (MongoDB / Firebase)


 🤝Contributing

Feel free to fork this repository and contribute by submitting a pull request.
