# Install and configure nfinx for servers

package { 'nginx':
  ensure => installed,
}

file { '/usr/share/nginx/html/index.html':
  content => 'Holberton School',
}

file { '/usr/share/nginx/html/404.html':
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  content =>
"server {
    listen 80;
    listen [::]:80 default_server;
    root   /usr/share/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://www.my80stv.com;
    }

    error_page 404 /404.html;
    location /404 {
        root /usr/share/nginx/html;
        internal;
    }
}",
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}

exec { 'nginx_reload':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
