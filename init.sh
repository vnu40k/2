#!/bin/bash

#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask


sudo /etc/init.d/mysql restart
#MySQL initial actions
mysql -uroot -e"CREATE DATABASE stepic"
mysql -uroot -e"CREATE USER 'admin'@'localhost' IDENTIFIED BY 'qwerty'"
mysql -uroot -e"GRANT ALL ON stepic.* TO 'admin'@'localhost'"

sudo python /home/box/web/ask/manage.py syncdb

sudo /etc/init.d/gunicorn restart
