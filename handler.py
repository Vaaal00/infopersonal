import json


def info(event, context):
    body = {
        "nombre": "Valeria Ceron", "edad": "19 años"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
