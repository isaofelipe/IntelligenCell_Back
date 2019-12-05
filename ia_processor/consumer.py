#!/usr/bin/env python
import os
os.chdir('..')

import pika
import time
from random import randrange
import jsonpickle
from ia_processor.retinanet.analyzer import Analyzer
from ia_processor.webserver import app
from cv2 import imwrite
from PIL import Image
from io import StringIO
from django.core.files.base import ContentFile
from django.core.files import File

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='analysis')


def callback(ch, method, properties, body):
    response = jsonpickle.loads(body.decode('utf-8'))
    image_path = response['image_path']
    process_id = response['process_id']

    print(" [x] The image ID (%s) is ready for analysis." % process_id)

    # process the image
    analyzer = Analyzer(image_path=image_path)
    analyzer = jsonpickle.encode(analyzer.find_objects())
    analyzer = jsonpickle.loads(analyzer)
    image_processed_path = os.path.join(app.config['UPLOAD_FOLDER'], '%s%s' % (process_id, '_processed.png'))

    # save the image
    imwrite(image_processed_path, analyzer['draw'])
    # imagem_processada = Image.open(image_processed_path)
    # img_io = StringIO()
    # imagem_processada.save(img_io, format='PNG', quality=100)
    # img_content = ContentFile(img_io.getvalue(), 'teste.png')

    imagem_processada = File(open(image_processed_path, 'rb'))

    # resposta
    response = {
        "message": "Imagem processada",
        "data": {"img_content": imagem_processada}
    }
    response_codificada = jsonpickle.encode(response)
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=response_codificada)
    ch.basic_ack(delivery_tag=method.delivery_tag)

    time.sleep(randrange(0, 5))
    print(" [x] The image ID (%s) has been successfully processed." % process_id)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback,
                      queue='analysis')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
