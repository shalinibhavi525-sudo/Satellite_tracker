from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# N2YO API settings
API_KEY = "DEMO_KEY"  # Replace with your own free key from n2yo.com if you want
BASE_URL = "https://api.n2yo.com/rest/v1/satellite/positions"

# Satellite IDs (ISS = 25544, Starlink example = 44238)
SATELLITES = {
    "ISS": 25544,
    "Starlink": 44238
}

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    satellite_name = None

    if request.method == "POST":
        satellite_name = request.form["satellite"]
        lat = request.form["latitude"]
        lon = request.form["longitude"]

        # Build API request
        url = f"{BASE_URL}/{SATELLITES[satellite_name]}/{lat}/{lon}/0/1/?apiKey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["positions"][0]  # Take first position result

    return render_template("index.html", data=data, satellite_name=satellite_name)

if __name__ == "__main__":
    app.run(debug=True)
