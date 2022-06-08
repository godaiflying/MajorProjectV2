#pip install flasksocketio
#https://blog.miguelgrinberg.com/post/learn-socket-io-with-python-and-javascript-in-90-minutes
#https://medium.com/geekculture/making-your-own-chatroom-sockets-in-python-javascript-html-ac14c2870064
#https://flask-socketio.readthedocs.io/en/latest/getting_started.html#initialization
#https://devcenter.heroku.com/articles/heroku-cli
#log into heroku

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socket = SocketIO(app)

@app.route('/')
def index():
    return render_template('client.html')

@socket.on('connect')
def connect():
    print("[CLIENT CONNECTED]:", request.sid)


@socket.on('disconnect')
def disconnect():
    print("[CLIENT DISCONNECTED]:", request.sid)

    
@socket.on('notify')
def notify(user):
    emit('notify', user, broadcast=True, skip_sid=request.sid)


@socket.on('data')
def emitback(data):
    emit('returndata', data, broadcast=True)


if __name__ == "__main__":
    socket.run(app)

