-- Creates the application user with access to the webshop database

CREATE USER IF NOT EXISTS 'ormuser'@'%' IDENTIFIED BY 'ormpass123';

GRANT ALL PRIVILEGES ON webshop.* TO 'ormuser'@'%';

FLUSH PRIVILEGES;
