#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
echo "
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name _;
	add_header X-Served-By $HOSTNAME;
	root   /var/www/html;
	index  index.html index.htm;
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}
}
" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
