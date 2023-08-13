file { '/var/www/html/wp-settings.php':
  ensure => present,
}

file_line { 'replace_line':
  ensure => present,
  line   => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  match  => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  path   => '/var/www/html/wp-settings.php',
}
