from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Route to save location
@app.route('/save_location', methods=['POST'])
def save_location():
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    # Check if the location.txt file exists, and create it if it doesn't
    with open("location.txt", "a") as file:
        file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
    
    return jsonify({"message": "Location saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
