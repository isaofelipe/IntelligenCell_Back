#!/usr/bin/env python
import jsonpickle
import pika


class IAProcessorProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='analysis')

    def call(self, body):
        response = jsonpickle.loads(body)

        self.channel.basic_publish(exchange='',
                                   routing_key='analysis',
                                   body=str(body))
        print(" [x] The image ID (%s) has been submitted for analysis.'" % response['process_id'])
        self.connection.close()
