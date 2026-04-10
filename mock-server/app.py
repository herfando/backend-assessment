from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_customers():
    with open("data/customers.json") as f:
        return json.load(f)

# HEALTH
@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

# GET ALL (PAGINATION)
@app.route("/api/customers")
def get_customers():
    data = load_customers()

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    paginated = data[start:end]

    return jsonify({
        "data": paginated,
        "total": len(data),
        "page": page,
        "limit": limit
    })

# GET BY ID
@app.route("/api/customers/<id>")
def get_customer(id):
    data = load_customers()

    customer = next((c for c in data if c["customer_id"] == id), None)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)