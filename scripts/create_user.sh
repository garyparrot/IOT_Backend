#!/usr/bin/env bash

echo -n "Username: "
read username

echo -n "Password: "
read password

mysql -e "CREATE USER '${username}'@'localhost' IDENTIFIED BY '${password}';"
mysql -e "GRANT ALL PRIVILEGES ON *.* TO '${username}'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"

