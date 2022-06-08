#!/bin/sh     
sudo git pull origin master
docker-compose up --force-recreate
