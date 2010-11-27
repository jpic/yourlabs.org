#!/bin/sh

PROJECT_ROOT=/srv/yourlabs.org/main

. $PROJECT_ROOT/../env/bin/activate

cd $PROJECT_ROOT
python manage.py update_all_feeds >> $PROJECT_ROOT/../log/cron_pull_posts.log 2>&1
