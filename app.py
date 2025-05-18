from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/')
def home():
    return "Flask backend is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    # Logic for responding to "Hi"
    if user_message.lower() == 'hi':
        return jsonify({'reply': 'Hello'})
    else:
        return jsonify({'reply': "I'm just a demo bot 😄"})

if __name__ == '__main__':
    app.run(debug=True)
