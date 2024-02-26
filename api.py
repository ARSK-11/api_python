from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []



@app.route('/post_data', methods=['POST'])
def post_data():
    try:
        if request.method == 'POST':
            req_data = request.json

            img = req_data.get('img')
            username = req_data.get('username')
            email = req_data.get('email')
            password = req_data.get('password')
            content = req_data.get('content')

            data.append({
                'img': img,
                'username': username,
                'email': email,
                'password': password,
                'content': content
            })

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

            return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
