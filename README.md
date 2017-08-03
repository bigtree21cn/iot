
## Introduction
Implement a IoT device event backend and frontend. It supports restful API and MQTT(to be done) to push the data from device to backend.
Backend support different database e.g. sqlite3, MySQL etc. A lightweight front-end is also going to implement and use to fetch  data from backend
to a web page.  Data pushing and fetching supports both user and device authentication.


## Build and Deploy


1. pull source code
2. goto the source root directory
```
sudo docker build -t iot .
```
3. running the service
```
sudo docker run --name myiot -d -p 5000:5000
sudo docker run --name myiot -d -p 5555:5000 -v /home/jefli/PycharmProjects/tmp/local_config.py:/opt/www/local_config.py  -v <yourdir>:/data/ iot
```
Note:
In development environment, its will use sqllite database. If you want to chagne the database, please change the database connection in local_config.py

4. create database
```
sudo docker exec myiot python3 manage.py CreateDB
```

## API Documentation

### The Rest API is described on swagger.json
(Need to be completed)

### API Example:
#### User API
add a new user
> curl -i -X POST -H "Content-Type: application/json" -d '{"username":"ok","password":"python"}'

get a token with user name and password
> curl -u ok:python -i -X GET http://127.0.0.1:5000/api/token

get a resource (authenticate needed) with a token
> curl -u 'yourtoken' -i -X GET http://127.0.0.1:5000/api/resource

#### Measurement API
post a measurement record
'''
curl -i -X POST -u ok:python -H "Content-Type: application/json"  \
        --data '{"start_time":"2017-07-12T03:17:44.332", "device_id": 1, "mea_id": 1, "c1": 0.5, "c2": 1.5, "c3": 22 }' \
        http://127.0.0.1:5000/api/measurements/
'''

query measurement with one dev_id
> curl -i -X GET -u ok:python http://127.0.0.1:5000/api/measurements/?dev_id=1



