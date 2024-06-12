# This Puppet manifest configures Nginx to handle high load efficiently

exec { 'increase-worker-processes':
  command => 'sed -i "s/worker_processes 1;/worker_processes auto;/" /etc/nginx/nginx.conf',
  onlyif  => 'grep -q "worker_processes 1;" /etc/nginx/nginx.conf',
  notify  => Exec['reload-nginx'],
}

exec { 'increase-worker-connections':
  command => 'sed -i "s/worker_connections 768;/worker_connections 1024;/" /etc/nginx/nginx.conf',
  onlyif  => 'grep -q "worker_connections 768;" /etc/nginx/nginx.conf',
  notify  => Exec['reload-nginx'],
}

exec { 'set-keepalive-timeout':
  command => 'sed -i "s/keepalive_timeout 65;/keepalive_timeout 30;/" /etc/nginx/nginx.conf',
  onlyif  => 'grep -q "keepalive_timeout 65;" /etc/nginx/nginx.conf',
  notify  => Exec['reload-nginx'],
}

exec { 'reload-nginx':
  command     => 'service nginx reload',
  refreshonly => true,
}

