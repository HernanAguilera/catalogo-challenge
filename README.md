## catalogo-challenge-api

API generada en Pyhon 3.5 con django 2.0 y django-rest-framework

### Instalacion

Instalación de dependencias
```
pip install -r requirements.txt
```

Generar la estructura de la base de datos

```
python manage.py migrate
```

Agregar data inicial a la base de datos:

```
python manage.py loaddata core/fixtures/catalogos.js
python manage.py loaddata core/fixtures/areas.js
python manage.py loaddata core/fixtures/items.js
```

> estos seeders fueron generados a partir de la data suministrada en el archivo .csv con el script que puede verse en la siguiente dirección: https://gist.github.com/HernanAguilera/fe42f038d4b740edfce127e458eb6207

Ejecutar el proyecto
```
python manage.py runserver
```
