import pika
import json
from Solicitud import Cyph as cy  # Asegúrate de que cy.encrypt_json funcione correctamente

#Configuración de conexión
rabbit_host = '34.16.14.54'
rabbit_user = 'isis2503'
rabbit_password = '1234'

#Establecer conexión
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbit_host,
        credentials=pika.PlainCredentials(rabbit_user, rabbit_password)
    )
)
channel = connection.channel()

#Asegurar existencia de la cola
channel.queue_declare(queue='map_requests', durable=True, exclusive=False, auto_delete=False)

#Función para enviar mensajes a la cola map_requests
def enviar_a_map_requests(mensaje_dict):
    encrypted_body = cy.encrypt_json(mensaje_dict)
    channel.basic_publish(
        exchange='',
        routing_key='map_requests',
        body=encrypted_body,
        properties=pika.BasicProperties(delivery_mode=2)  # persistente
    )
    print("Mensaje enviado a map_requests")