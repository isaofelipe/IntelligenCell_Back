from __future__ import absolute_import

import os
from uuid import uuid4
from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename
import jsonpickle
from ia_processor.producer import IAProcessorProducer

# Flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['UPLOAD_FOLDER'] = 'uploads'
socket_io = SocketIO(app)

"""Flask implementation"""


@app.route('/')
def index():
    return render_template('session.html')


@app.route('/processor/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        response = {'message': 'Image was not received'}
        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=400, mimetype="application/json")

    image = request.files['image']
    image_id = uuid4().hex
    image_name = secure_filename('%s%s' % (image_id, '.png'))
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)

    # store the image on upload's folder
    image.save(image_path)

    process_response = jsonpickle.encode({
        'process_id': image_id,
        'image_path': image_path
    })

    ia_processor_producer = IAProcessorProducer()
    ia_processor_producer.call(process_response)

    # build a response dict to send back to client
    response = {
        'message': 'Image was received.',
        'data': {'process_id': image_id}
    }

    # encode response using json pickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


"""Web socket implementation"""


@socket_io.on('ia_processor_connect')
def connect():
    print('Frontend connected')


@socket_io.on('ia_processor_disconnect')
def disconnect():
    print('Frontend disconnected')


if __name__ == '__main__':
    socket_io.run(app, debug=True)
