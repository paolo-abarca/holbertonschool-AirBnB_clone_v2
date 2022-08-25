#!/usr/bin/env bash
# Adding Bash script that configures web servers for web_static implementation
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
new_string="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tindex index.html index.htm;\n\t}"

sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-available/default

sudo service nginx restart
