# iot


1. git pull all the source code
2. goto the source root directory
   # sudo docker build -t iot .
3. running the service
   #sudo docker run --name myiot -d -p 5000:5000 -v /yourdir/local_config.py:./local_config.py
   Note:
        In development environment, its will use sqllite database. If you want to chagne the database, please change the database
        connection in local_config.py
4. create database
   #sudo docker exec python3 manage.py createDB myiot

The API is described on swagger.json
Login
    <Todo>
Measurement
    <Todo>


