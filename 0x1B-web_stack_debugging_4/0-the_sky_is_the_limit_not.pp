# Task 0

file {'/etc/default/nginx':
  ensure  => present,
  path    =>  '/etc/default/nginx',
  content => 'ULIMIT="-n 4096"',
}

-> exec {'nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
