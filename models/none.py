from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {

        "username": "benedict",
        "details":
            [
                {
                    "age": 24,
                    "password": "king123$"

                }
            ]
    }
]


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})


@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    new_user = {

        "username": request_data['username'],
        "details": []}
    users.append(new_user)
    return jsonify(new_user)


@app.route('/user/<string:username>/details', methods=['POST'])
def add_user_details(username):
    request_data = request.get_json()
    for user in users:
        if users['username'] == username:
            new_details = {
                "age": request_data['age'],
                "password": request_data['password']
            }
        users['details'].append(new_details)
        return jsonify(new_details)
    return jsonify({"message": "user not found"})


if __name__ == "__main__":
    app.run()
