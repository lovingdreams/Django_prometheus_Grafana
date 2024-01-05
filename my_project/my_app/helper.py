from myproject.celery import app
from common.configs.config import config as cfg
import pika
import json


@app.task(queue=cfg.get("celery", "QUEUE"))
def backgroundTask(product_id, action):
    publish({"product_id": product_id, "action": action})


def publish(message):

    credentials = pika.PlainCredentials(
        cfg.get("rabbit_mq", "USER_NAME"), cfg.get("rabbit_mq", "PASSWORD")
    )
    parameters = pika.ConnectionParameters(
        host=cfg.get("rabbit_mq", "HOST"),
        virtual_host=cfg.get("rabbit_mq", "VIRTUAL_HOST"),
        credentials=credentials,
        frame_max=int(cfg.get("rabbit_mq", "FRAME_MAX")),
        heartbeat=int(cfg.get("rabbit_mq", "HEART_BEAT")),
        connection_attempts=int(cfg.get("rabbit_mq", "CONNECTION_ATTEMPTS")),
    )
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    # Declare the exchange (if not already declared)
    channel.exchange_declare(
        exchange='myprojectexchange',
        exchange_type='fanout'
    )

    # Publish the event to the exchange
    channel.basic_publish(
        exchange='myprojectexchange',
        routing_key='',
        body=json.dumps(message)
    )

    # Close the connection
    connection.close()
