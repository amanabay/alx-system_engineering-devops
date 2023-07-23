# Configure web_servers using puppet

exec { 'command':
  command => 'sudo apt-get update;
  sudo apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default; sudo service nginx -s reload',
  provider => shell,
}
