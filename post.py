import requests

# URL of your Flask application
url = 'http://localhost:5000/post_data'

# Sample data to post
data = {
    'img': 'image_data',
    'username': 'example_user',
    'email': 'example@example.com',
    'password': 'example_password',
    'content': 'example_content'
}

# Send POST request
response = requests.post(url, json=data)

# Print response
print(response.json())
