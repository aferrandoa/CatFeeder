#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scheduler.py
#  
#  
# 
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

def init_scheduler():
    '''Task scheduler initialization'''

def get_all_jobs():
    '''Get the list of scheduled jobs'''
    return scheduler.get_jobs()

def add_job(exe_func, job_name, sel_hour, sel_minute):
    '''Adds a job'''
    scheduler.add_job(exe_func, 'cron', hour=sel_hour, minute=sel_minute, name=job_name)

def remove_job(job_id):
    '''Removes a job'''
    scheduler.remove_job(job_id=job_id)

scheduler = BackgroundScheduler()
scheduler.configure(jobstores=jobstores)
scheduler.start()