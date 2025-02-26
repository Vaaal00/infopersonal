import json


def info(event, context):
    body = {
        "nombre": "Valeria Ceron", "codigo": "240220232008", "fecha nacimiento": "17/08/2005", "edad": "19 años", "correo": "valeria.ceron.0499@eam.edu.co", "direccion": "Quimbaya, Quindio"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
