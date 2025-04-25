# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)
latest_command = None

@app.route('/send', methods=['POST'])
def send():
    global latest_command
    latest_command = request.json.get('cmd')
    return jsonify({"status": "received", "command": latest_command})

@app.route('/get', methods=['GET'])
def get():
    global latest_command
    cmd = latest_command
    latest_command = None  # بعد از دریافت، دستور پاک میشه
    return jsonify({"command": cmd})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
