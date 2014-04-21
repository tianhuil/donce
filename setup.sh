#!/bin/bash

PASSWORD='skm39c82l9x'
echo $PASSWORD > ~/.mysql_donce_user_pw
echo "
CREATE DATABASE IF NOT EXISTS donce_db;
USE donce_db;
CREATE USER 'donce_user'@'localhost' IDENTIFIED BY '$PASSWORD';
GRANT ALL PRIVILEGES ON donce_db.* TO 'donce_user'@'localhost';
" | mysql -u root -p
echo "Done!"
