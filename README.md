# Proyecto Para la Api Urban Grocers 

Estaremos validando la creacion de un kit dentro de un usuario en particular y crearemos pruebas especificas para el campo (name), se crearan tests para revisar que los codigos de respuesta dados coincidan con los esperados utilizando la aplicacion de Urban Grocers.

Para ello nos apoyaremos en la documentacion que nos brindan para estudiar la API de la aplicacion que trabajaremos.

```sh
la URL del servdor iniciado>/docs/
```

Dentro de esta documentacion validaremos la siguiente fuente:
```sh
"Main.user"  para la creacion de un usuario
"Main.kits"  para la creacion de un kit
```

## Archivos requeridos 
- **configuration.py** Se almacena la URL y las rutas.
- **data.py** Se encontraran los cuerpos de las solicitudes POST.
- **sender_stand_request.py** Estaran las solicitudes que se necesitan para la creacion de un usuario y la creacion de un kit.
- **create_kit_name_kit_test.py**Contiene la lista de comprobacion completa incluyendo las solicitudes para prubeas positivas, pruebas negativas y los test de comprobacion.
- **README.md** Se encontrara una breve descripcion del proyecto.
- **.gitignore**  Sera la lista de archivos que queremos que Git ignore.


## Lista de comprobacion de pruebas 
Esta sera la lista a tener en cuenta para las comprobaciones que se realizaran.

N° | Descripcion  | Codigo de Respuesta 
---|------------------ | -------------
1 | El número permitido de caracteres (1): kit_body = { "name": "a"}l  |  kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2 | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
3 | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } | Código de respuesta: 400
4 | El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } | Código de respuesta: 400
5 | Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
6 | Se permiten espacios: kit_body = { "name": " A Aaa " } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7 | Se permiten números: kit_body = { "name": "123" } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
8 | El parámetro no se pasa en la solicitud: kit_body = { } | Código de respuesta: 400
9 | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } | Código de respuesta: 400

### A tener en cuenta
- Necesitaras instalar los paquetes **pytest** y **request** para ejecutar las pruebas.
- Se debe iniciar regularmente el servidor de Urban Grocers y actualizar la variable de la 'URL_SERVICE' del archivo 'configuration.py' para poder ejecutar las pruebas.
- Ejecutaras las pruebas del proyecto atraves de la terminal pycharm escribiendo: **pytest**.
- Algunas pruebas devolverán FAILED como resultado; no te preocupes, es un comportamiento esperado dentro de la lista de comprobaciones.