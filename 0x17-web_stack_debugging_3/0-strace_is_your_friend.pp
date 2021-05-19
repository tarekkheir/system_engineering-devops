# Fix settings by adding line in wp-settings.php
exec { 'correction': 
  command => 'sed -i "/phpp/php/g" /var/www/html/wp-settings.php'
  path => '/usr/bin/:/bin:usr/bin/env'
}
