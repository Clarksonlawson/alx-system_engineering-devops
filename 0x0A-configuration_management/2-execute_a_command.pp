# Puppet Manifest to kill a process named killmenow
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

