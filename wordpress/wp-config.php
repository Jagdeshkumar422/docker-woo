<?php
define('DB_NAME', 'wordpress'); // Database name

define('DB_USER', 'wordpress'); // Database user (not root)
define('DB_PASSWORD', 'wordpress'); // Database password (as per Docker Compose)
define('DB_HOST', 'mysql'); // The service name of MySQL in Docker

define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');

// Security keys (generate new ones from https://api.wordpress.org/secret-key/1.1/salt/)
define('AUTH_KEY',         'your_random_key_here');
define('SECURE_AUTH_KEY',  'your_random_key_here');
define('LOGGED_IN_KEY',    'your_random_key_here');
define('NONCE_KEY',        'your_random_key_here');
define('AUTH_SALT',        'your_random_key_here');
define('SECURE_AUTH_SALT', 'your_random_key_here');
define('LOGGED_IN_SALT',   'your_random_key_here');
define('NONCE_SALT',       'your_random_key_here');

// WordPress debugging mode
define('WP_DEBUG', false);

// Absolute path to the WordPress directory
if (!defined('ABSPATH')) {
    define('ABSPATH', dirname(__FILE__) . '/');
}

// Sets up WordPress vars and included files
require_once ABSPATH . 'wp-settings.php';
