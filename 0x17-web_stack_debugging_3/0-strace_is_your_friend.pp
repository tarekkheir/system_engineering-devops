# Fix Wordpress file
exec { 'correction': 
  command =>  "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  'usr/bin/:/bin:usr/bin/env'
}
