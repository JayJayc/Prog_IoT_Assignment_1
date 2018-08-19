#!/usr/bin/env python3
from crontab import CronTab

# init cron
cron = CronTab(user='pi')
cron.remove_all()

# add new cron job
job = cron.new(command='/home/pi/IoT/Assignment1/logger.py')

# job settings
job.minute.every(60*6)
cron.write()
