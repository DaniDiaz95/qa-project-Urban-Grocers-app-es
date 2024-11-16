import data
import configuration
import requests

# funcion para crear un Usuario
def post_new_user(user_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body, #insertar el cuerpo de la solicitud en formato json
        headers=data.headers
    )

#print(post_new_user({'firstName': 'ab', 'phone': '+10005553535', 'address': '8042 Lancaster Ave.Hamburg, NY'}).json())

# funcion para crear un Kit
def post_new_kit(kit_body):
    # creo mi **valor para tomar el token de la creacion de usuario
    user_token = post_new_user(data.user_body).json() #defino mi funcion en formato json
    headers = data.headers #llamo a mi variable headers
    # al encabezado le añado la nueva clave Authorization donde el valor de authtoken es tomado de la variable user_token
    headers['Authorization'] = 'Bearer ' + user_token['authToken']

    return requests.post(
       configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )
