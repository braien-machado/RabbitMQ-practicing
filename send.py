import pika, sys, os

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get('RABBITMQ_HOST')))
channel = connection.channel()
channel.queue_declare(queue='queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World!'

channel.basic_publish(
    exchange='',
    routing_key='queue',
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
)

print(f' [x] Sent {message}')

connection.close()
