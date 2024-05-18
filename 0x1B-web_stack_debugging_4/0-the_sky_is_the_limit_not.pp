# Puppet manifest to optimize Nginx server for high load

exec { 'increase_nginx_limits':
  command => 'sed -i "/^http {/a \\    client_max_body_size 10M;\n    keepalive_timeout 65;" /etc/nginx/nginx.conf',
  unless  => 'grep -q "client_max_body_size 10M" /etc/nginx/nginx.conf',
  notify  => Exec['reload_nginx'],
}

exec { 'increase_worker_processes':
  command => 'sed -i "/^http {/a \\    worker_processes auto;\n    events {\n        worker_connections 1024;\n    }" /etc/nginx/nginx.conf',
  unless  => 'grep -q "worker_processes auto" /etc/nginx/nginx.conf',
  notify  => Exec['reload_nginx'],
}

exec { 'reload_nginx':
  command     => 'service nginx reload',
  refreshonly => true,
}

