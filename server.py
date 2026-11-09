from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

room = set()

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@socketio.on("connect")
def on_connect():
    if len(room) >= 2:
        return False
    room.add(request.sid)
    socketio.emit("peer-count", {"count": len(room)})

@socketio.on("disconnect")
def on_disconnect():
    room.discard(request.sid)
    socketio.emit("peer-count", {"count": len(room)})
    socketio.emit("peer-left", skip_sid=request.sid)

@socketio.on("offer")
def handle_offer(data):
    socketio.emit("offer", data, skip_sid=request.sid)

@socketio.on("candidate")
def handle_candidate(data):
    socketio.emit("candidate", data, skip_sid=request.sid)

@socketio.on("answer")
def handle_answer(data):
    socketio.emit("answer", data, skip_sid=request.sid)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
