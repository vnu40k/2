#!/bin/bash
curDir=$(pwd)
homeEnv='/home/user/StepicWebTech/web'
testEnv='/home/box/web'


if [ $curDir == $homeEnv ]; then
        echo 'home env'

	sudo ln -s /home/user/StepicWebTech/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
	sudo /etc/init.d/nginx restart

	cd ask
	sudo gunicorn -b 127.0.0.1:8000 ask.wsgi
elif [ $curDir == $testEnv ]; then
        echo 'test env'

	./createDB.sh
	
	sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
	sudo rm -rf /etc/nginx/sites-enabled/default
	sudo /etc/init.d/nginx restart

	sudo ln -sf ~/web/etc/gunicorn.conf   /etc/gunicorn.d/test
	sudo /etc/init.d/gunicorn restart

	cd ~/web/ask/ask
	gunicorn -b 127.0.0.1:8000 wsgi

else
        echo 'unknown env!'
	exit
fi

