import pika
#import Cyph as cy
from .cifr import encrypt_json

def get_channel():
    rabbit_host = '10.128.0.20'
    rabbit_user = 'isis2503'
    rabbit_password = '1234'
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=rabbit_host,
            credentials=pika.PlainCredentials(rabbit_user, rabbit_password)
        )
    )
    return connection.channel()

def enviar_a_map_requests(mensaje_dict):
    channel = get_channel()
    channel.queue_declare(queue='map_requests', durable=True, exclusive=False, auto_delete=False)
    channel.basic_publish(
        exchange='',
        routing_key='map_requests',
        body=encrypt_json(mensaje_dict),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    channel.close()