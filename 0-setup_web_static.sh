#!/usr/bin/env bash
# Sets up web servers for deployment of web_static

# Install nginx if not installed
sudo apt-get update -y
sudo apt-get install -y nginx

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R $(whoami):$(id -gn) /data/

# Update Nginx configuration to serve content
nginx_conf="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" "$nginx_conf"; then
  sudo sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" "$nginx_conf"
fi

# Restart Nginx
sudo service nginx restart

exit 0

