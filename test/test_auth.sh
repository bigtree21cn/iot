

# add a new user
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"ok","password":"python"}'

#get a token with user name and password
curl -u ok:python -i -X GET http://127.0.0.1:5000/api/token

#get a resource (authenticate needed) with a token
curl -u 'yourtoken' -i -X GET http://127.0.0.1:5000/api/resource


