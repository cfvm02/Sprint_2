from flask import Flask, request, jsonify
import pika
from cifr import encrypt_json  # Asegúrate de que este módulo esté en tu proyecto

app = Flask(__name__)

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
    return connection.channel(), connection

@app.route('/enviar', methods=['POST'])
def enviar():
    mensaje_dict = request.get_json()
    if not mensaje_dict:
        return jsonify({"error": "No se proporcionó un JSON válido"}), 400

    try:
        channel, connection = get_channel()
        channel.queue_declare(queue='map_requests', durable=True, exclusive=False, auto_delete=False)
        channel.basic_publish(
            exchange='',
            routing_key='map_requests',
            body=encrypt_json(mensaje_dict),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        channel.close()
        connection.close()
        return jsonify({"mensaje": "Mensaje enviado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": f"No se pudo enviar el mensaje: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
