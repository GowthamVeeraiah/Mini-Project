from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Karnataka districts (for validation / realism)
KARNATAKA_DISTRICTS = [
    "Bagalkote","Ballari","Belagavi","Bengaluru Rural","Bengaluru Urban",
    "Bidar","Chamarajanagar","Chikkaballapura","Chikkamagaluru",
    "Chitradurga","Dakshina Kannada","Davanagere","Dharwad","Gadag",
    "Hassan","Haveri","Kalaburagi","Kodagu","Kolar","Koppal","Mandya",
    "Mysuru","Raichur","Ramanagara","Shivamogga","Tumakuru","Udupi",
    "Uttara Kannada","Vijayanagara","Vijayapura","Yadgir"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getAQI", methods=["POST"])
def get_aqi():
    data = request.get_json()
    city = data.get("city")
    condition = data.get("condition")

    # Safety check
    if city not in KARNATAKA_DISTRICTS:
        return jsonify({
            "aqi": 0,
            "advice": "Invalid district selected."
        })

    # Simulated AQI values (realistic range)
    aqi = random.randint(40, 180)

    # Health-based advice
    if aqi <= 50:
        advice = f"Air quality in {city} is good. Safe for {condition} patients."
    elif aqi <= 100:
        advice = f"Air quality in {city} is moderate. {condition} patients should limit outdoor activity."
    else:
        advice = f"Air quality in {city} is poor. {condition} patients should stay indoors."

    return jsonify({
        "aqi": aqi,
        "advice": advice
    })

# Local run (Render will ignore this and use gunicorn)
if __name__ == "__main__":
    app.run(debug=True)
