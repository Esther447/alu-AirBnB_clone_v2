#!/usr/bin/env bash
# Sets up web servers for deployment of web_static

# Install Nginx if it's not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update -y
    apt-get install nginx -y
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership
chown -R ubuntu:ubuntu /data/

# Update Nginx config
NGINX_CONF="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$NGINX_CONF"; then
    sed -i "/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" "$NGINX_CONF"
fi

# Restart Nginx
service nginx restart

exit 0
