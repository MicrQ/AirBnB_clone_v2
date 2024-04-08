# a puppet script that sets a web_static for deployment.

$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.nginx-debian.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://linkedin.com/in/abenetg;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure => installed,
}
file { '/data':
  ensure => 'directory',
}
file { '/data/web_static':
  ensure => 'directory',
}
file { '/data/web_static/releases':
  ensure => 'directory',
}
file { '/data/web_static/shared':
  ensure => 'directory',
}
file { '/data/web_static/releases/test':
  ensure => 'directory',
}
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School',
}
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}
exec { 'owner':
  command => 'sudo chown -hR ubuntu:ubuntu /data/'
}
file { '/var/www':
  ensure => 'directory'
}

file { '/var/www/html':
  ensure => 'directory'
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
}
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'present',
  content => $nginx_conf,
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}
