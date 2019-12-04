#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:22:53 2019.

@author: dmitriy
"""
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

cmd ="python3 itcfinally2.py"
subprocess.call(cmd, shell=True)
cmd = "python3 app.py"
subprocess.call(cmd, shell=True)


sched = BlockingScheduler(timezone="Europe/Kiev")

'''
@sched.scheduled_job('interval', minutes=25)
def timed_job():
    """Select time interval."""
    print('This job is run every three minutes.')
    cmd = "python3 itcfinally2.py"
    subprocess.call(cmd, shell=True)
    print("Complete!")
'''

# timed_job()


# job = sched.scheduled_job(timed_job(), 'interval', minutes=1)
# del job


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=20, minute=00)
def scheduled_job():
    """Schedule a job."""
    print('This job is run every weekday at 5pm.')
    cmd = "python3 itcfinally2.py"
    subprocess.call(cmd, shell=False)


sched.start()
# sched.shutdown()
