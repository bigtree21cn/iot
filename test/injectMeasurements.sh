#!/usr/bin/env bash



function rand(){  
	min=$1
	max=$(($2-$min+1))
	num=$(date +%s%N)
	echo $(($num%$max+$min))
}



#post a measurement record
while True; do

json="{\"device_id\": 1, \"mea_id\": $(rand 1 2), \"c1\": $(rand 0 100), \"c2\": $(rand 0 100), \"c3\": $(rand 0 100)}"
echo $json

curl -i -X POST -u jefli:123456 -H "Content-Type: application/json"  \
	--data "${json}" \
        http://127.0.0.1:5000/api/measurements/
sleep 5
done

