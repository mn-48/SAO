import pika
import json

# https://api.cloudamqp.com/console/94103386-d050-42ea-813d-624c2d0f6650/details

# nBHT9vAr8BRq720r6fhTx1mbxaLPw3Lc

# amqps://tkhntmuh:nBHT9vAr8BRq720r6fhTx1mbxaLPw3Lc@cow.rmq2.cloudamqp.com/tkhntmuh
params = pika.URLParameters(
    'amqps://tkhntmuh:nBHT9vAr8BRq720r6fhTx1mbxaLPw3Lc@cow.rmq2.cloudamqp.com/tkhntmuh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
