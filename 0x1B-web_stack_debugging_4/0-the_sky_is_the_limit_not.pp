# Execute command to modify Nginx's maximum open files limit and restart Nginx service. 

exec { 'modify_nginx_files_limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
