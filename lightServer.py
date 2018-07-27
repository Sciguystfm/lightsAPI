from flask import Flask
from flask import request
import json
from hueAPI import HueController
app = Flask(__name__)
rooms = {
    "1":"Kitchen",
    "2":"Living",
    "3":"Bedroom"
}
hue = HueController('192.168.86.132')

@app.route('/')
def homepage():
    return 'Hello, World!'


@app.route('/normalize', methods=['POST'])
def normalize():
    rooms = json.loads(request.data)['rooms']
    print(rooms)
    hue.normalizeRooms(rooms)
    return "Normalized"

@app.route('/off', methods=['POST'])
def off():
    rooms = json.loads(request.data)['rooms']
    hue.turnRoomsOff(rooms)
    return "Turned Off"

@app.route('/nightlight', methods=['POST'])
def nightlight():
    rooms = json.loads(request.data)['rooms']
    hue.nightlight(rooms)
    return "Turned Off"

def main():
    app.run(host='0.0.0.0', port=6700)


if __name__ == '__main__':
    main()