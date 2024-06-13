# Increase the ULIMIT of the default file for Nginx
exec { 'increase-ulimit':
  command => 'sed -i "s/^ULIMIT=.*/ULIMIT=4096/" /etc/default/nginx',
  onlyif  => 'grep -q "^ULIMIT=15" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  notify  => Exec['nginx-restart'],
}

# Restart Nginx to apply changes
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => ['/etc/init.d', '/usr/sbin', '/usr/bin', '/sbin'],
  refreshonly => true,
}
