
data_path=~/mysql/data/
if [ -f data_path ]; then
    mkdir -p data_path
fi


sudo docker run --name mysql -v $data_path:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
