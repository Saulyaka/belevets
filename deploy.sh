#!/bin/sh     
sudo git pull https://github.com/saulyaka/belevets.git
docker-compose down -v
sudo docker-compose up --force-recreate
