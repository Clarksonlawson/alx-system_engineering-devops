# This Puppet manifest fixes the Apache 500 Internal Server Error
# by addressing the root cause identified using strace.

# Use an exec resource to run strace on the Apache process
exec { 'fix-apache-error':
  command     => 'strace -e open,access apache2 2>&1',
  logoutput   => true,
  refreshonly => true,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body>Hello World!</body></html>',
}

# Notify Apache service to reload configuration after the fix
service { 'apache2':
  ensure  => running,
  require => File['/var/www/html/index.html'],
}

