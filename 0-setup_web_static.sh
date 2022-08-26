#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
search="^\t\}$"
adding="\t\}\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"

sudo sed -i "0,/$search/s//$adding/" /etc/nginx/sites-available/default
sudo service nginx restart
