#!/bin/bash
echo "Starting MySQL server..."
sudo /etc/init.d/mysql start
echo "Creating DB if not exists..."
mysql -u root -e "create database if not exists askpupkin_db;"
mysql -u root -e "grant all on askpupkin_db.* to 'user'@'localhost' identified by 'q1';"
mysql -u user -p -e "SHOW DATABASES;"
echo "Running Django scripts..."
echo "Validating models..."
cd /home/box/web/ask
./manage.py validate
echo "Creating tables..."
./manage.py syncdb
echo "DONE!"
