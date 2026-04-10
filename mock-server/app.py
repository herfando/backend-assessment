from flask import Flask, jsonify
import json

app = Flask(__name__)

# load data dari JSON
def load_customers():
    with open("data/customers.json") as f:
        return json.load(f)

# health check
@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

# get semua customer
@app.route("/api/customers")
def get_customers():
    data = load_customers()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)