from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alice"}
]

# Home
@app.route("/")
def home():
    return jsonify({"message": "Welcome To User API"})

# Get all users
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify({"users": users})

# Get user by ID
@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Add user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added", "user": data})

# Update user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    for user in users:
        if user["id"] == id:
            user["name"] = data.get("name", user["name"])
            return jsonify({
                "message": "User updated",
                "user": user
            })
    return jsonify({"error": "User not found"}), 404

# Delete user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    for i in range(len(users)):
        if users[i]["id"] == id:
            deleted = users.pop(i)
            return jsonify({"message": "User deleted", "user": deleted})
    return jsonify({"error": "User not found"}), 404

# Run server
if __name__ == "__main__":
    app.run(debug=True)