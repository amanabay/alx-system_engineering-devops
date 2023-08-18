# Puppet manifest to modify the OS security configuration
# This manifest replaces occurrences of the "holberton" user with "Ken" in the /etc/security/limits.conf file.

exec { 'modify_security_config':
  command => 'sed -i "s/holberton/Ken/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
