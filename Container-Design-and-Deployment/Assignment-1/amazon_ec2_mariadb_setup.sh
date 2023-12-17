#!/bin/bash

SECURE_MYSQL=$(expect -c "
set timeout 3
spawn mysql_secure_installation
expect \"Enter current password for root (enter for none):\"
send \"\r\"
expect \"Enable unix_socket authentication?\"
send \"y\r\"
expect \"Change the root password?\"
send \"y\r\"
expect \"New password:\"
send \"test1234\r\"
expect \"Re-enter new password:\"
send \"test1234\r\"
expect \"Remove anonymous users?\"
send \"y\r\"
expect \"Disallow root login remotely?\"
send \"y\r\"
expect \"Remove test database and access to it?\"
send \"y\r\"
expect \"Reload privilege tables now?\"
send \"y\r\"
expect eof
")

#
# Execution mysql_secure_installation
#
echo "${SECURE_MYSQL}"
