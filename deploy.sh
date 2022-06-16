#!/bin/sh     
sudo git pull https://github.com/saulyaka/belevets.git
sudo docker-compose down -v
sudo docker-compose -f belevets/docker-compose.yml up --build
