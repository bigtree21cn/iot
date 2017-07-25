#!/usr/bin/env bash

#post a measurement record
curl -i -X POST -u jefli:123456 -H "Content-Type: application/json"  \
        --data '{"start_time":"2017-07-12T03:17:44.332", "device_id": 1, "mea_id": 1, "c1": 0.5, "c2": 1.5, "c3": 22 }' \
        http://127.0.0.1:5000/api/measurements/

#query measurement with one dev_id
curl -i -X GET -u jefli:123456 http://127.0.0.1:5000/api/measurements/?dev_id=1

