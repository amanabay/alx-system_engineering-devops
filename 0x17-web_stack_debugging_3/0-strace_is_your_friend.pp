# Fix wp-settings.php by replace wrong extension(phpp) by php

exec { 'replace_phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path => ['/usr/bin/']

}
