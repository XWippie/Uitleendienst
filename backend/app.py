from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, request, jsonify
from repositories.DataRepository import DataRepository

# Code voor Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '5)FK33KFF@fg@édfgs'

socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# Handles the default namespace
@socketio.on_error()
def error_handler(e):
    print(e)

# API ENDPOINTS
endpoint = '/api/v1'

@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."
    
    
# socketio
@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    
        
# ANDERE FUNCTIES*
if __name__ == '__main__':
    try:
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
            
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')

