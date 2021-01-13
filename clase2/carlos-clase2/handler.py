import json


def hello(event, context):
    print(event)
    body = {"nombre": "Carlos", "event": event}
    response = {"statusCode": 200, "body": "hey guapo desde el server!"}

    return response
