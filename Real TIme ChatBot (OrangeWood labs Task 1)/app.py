from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    processed_data = process_message(message)  # Implement your processing logic here
    send(processed_data, broadcast=True)

def process_message(message):
    # Implement your processing logic here
    # For demonstration, let's just return the reversed message
    return message[::-1]

if __name__ == '__main__':
    socketio.run(app, debug=True)
