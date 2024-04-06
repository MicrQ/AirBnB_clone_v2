#!/usr/bin/env bash
# a bash script that sets up the web-static for deployment.
sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf  /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '29i \\n location /hbnb_static {\n\t alias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
