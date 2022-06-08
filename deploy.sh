#!/bin/sh     
sudo git pull origin master
docker-compose down -v
sudo docker-compose up --force-recreate
touch test11111.txt
