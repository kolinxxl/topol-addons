from flask import Flask, jsonify
import requests
from topol_parser import parse_response

app = Flask(__name__)

DEVICE_URL = "http://10.0.0.1/status_read"
PAYLOAD = "t=timestamp&l=18&p=1&i=11050&d=0"

@app.route("/topol/status", methods=["GET"])
def get_topol_status():
    try:
        response = requests.post(DEVICE_URL, data=PAYLOAD, headers={"Content-Type": "text/plain"}, timeout=5)
        response.raise_for_status()
        parsed_data = parse_response(response.text)
        return jsonify(parsed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
