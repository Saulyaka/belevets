#!/bin/sh     
sudo git pull https://github.com/saulyaka/belevets.git
sudo docker-compose down -v
sudo docker-compose -f home/ec2-user/belevets/docker-compose.yml up --build
