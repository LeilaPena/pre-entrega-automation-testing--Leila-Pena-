import requests
import pytest
import logging
from faker import Faker
import pathlib


#Configuración
URL_base = "https://jsonplaceholder.typicode.com"
fake= Faker()
path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename= path_dir/ "historial.log",
    level= logging.INFO,
    format= '%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt= '%H:%M:%S'
)
file_handler = logging.FileHandler(path_dir / "historial.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)

file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

logger = logging.getLogger()

class TestJSONPlaceholder:

    #Metodo GET - obtener todos los posts - caso éxito
    def test_get_posts_success(self):
        logger.info("\n=== Test 1: GET Posts===")

        #Petición GET y validación del código de estado
        response = requests.get(f"{URL_base}/posts")
        assert response.status_code == 200,  f"Esperando código 200, código obtenido : {response.status_code}"
        logger.info("Código de estado 200")

        #Convertir a JSON y validación de estructura
        data = response.json()
        assert isinstance(data, list), "La respuesta debería ser una lista"
        assert len(data) > 0, "La  lista no debería estar vacia"
        logger.info('Estructura JSON correcta')

        #Validación de la estructura del primer post
        first_post = data[0]
        required_fields = ["userId","id","title","body"]
        for field in required_fields:
            assert field in first_post, f"Campo '{field}' no encontrado"
        logger.info("Estructura del post correcta")

        #Validación del tipo de datos
        assert isinstance(first_post['id'], int)
        assert isinstance(first_post["title"], str)
        assert isinstance(first_post['body'], str)
        logger.info("Tipos de datos correctos")

        logger.info('Metodo GET completado exitosamente')

    #Metodo POST - crear un nuevo post - caso éxito
    def test_create_post_succes(self):
        logger.info("\n=== Test 2: POST post===")

        #Datos de FAKER para crear  el post
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }

        #Petición POST y validación del código de estado
        response = requests.post(f"{URL_base}/posts", json=post_data)
        assert response.status_code == 201,  f"Esperando código 201, código obtenido : {response.status_code}"
        logger.info("Código de estado 201")

        #Convertir a JSON y validación de estructura
        data = response.json()
        expected_fields = ["userId","id","title","body"]
        for field in expected_fields:
            assert field in data, f"Campo '{field}' no encontrado"
        logger.info("Estructura correcta")

        #Validación de los datos guardados
        assert data["title"] == post_data["title"]
        assert data["body"] == post_data["body"]
        assert data["userId"] ==  post_data["userId"]
        assert data["id"] == 101,f"Esperando código 101, código obtenido: {data['id']}"
        logger.info("Datos guardados correctamente, ID asignado corrrectamente")

        logger.info('Metodo POST completado exitosamente')
    
    #Metodo DELETE - borrar un post - caso éxito
    def test_delete_post_success(self):
        logger.info("\n=== Test 3: DELETE post===")

        #ID del post a eliminar (usamos uno que sabemos que existe porque JSON Placeholder no almacena datos)
        post_id=1

        #Petición DELETE y validación del código de estado
        response = requests.delete(f"{URL_base}/posts/{post_id}")
        assert response.status_code == 200, f"Esperando código 200, código obtenido: {response.status_code}"
        logger.info("Código de estado 200")

        #Convertir a JSON y verificar que devuelva un objeto vacio
        data = response.json()
        assert data == {}, f"Esperado un diccionario vacio, obtenido {data}"
        logger.info("Respuesta DELETE correcta")

        logger.info('Metodo DELETE completado exitosamente')