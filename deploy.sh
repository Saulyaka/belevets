#!/bin/sh     
sudo git pull origin master
docker-compose down -v
docker-compose up --force-recreate
touch test.txt
