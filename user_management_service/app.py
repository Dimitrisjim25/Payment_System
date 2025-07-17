from flask import Flask, jsonify, request
from typing import Dict, List, Any

app = Flask(__name__)

# Αποθήκευση χρηστών σε μνήμη
users: List[Dict[str, Any]] = []

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    user = request.get_json()
    users.append(user)
    return jsonify({"message": "User added", "user": user}), 201

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    if user_id < len(users):
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
