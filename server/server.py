#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  	server.py
# 	PiCam Local Web Server with Flask

from flask import Flask, render_template, Response, jsonify, url_for, request
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, roles_required
from security.database import db_session, init_db
from security.models import User, Role
import json

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
import engine
import database
import scheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret'

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    init_db()

@app.route('/')
@login_required
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
@roles_required('FULL')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
					
@app.route('/open_action')
@roles_required('FULL')
def open_action():
    """Test action url"""
    engine.open_door()
    print("Action done")
    return jsonify(result="")
	
@app.route('/close_action')
@roles_required('FULL')
def close_action():
    """Test action url"""
    engine.close_door()
    print("Action done")
    return jsonify(result="")

@app.route('/get_jobs')
@roles_required('FULL')
def get_jobs():
    """Get jobs list"""
    jobs_list = scheduler.get_all_jobs()

    if len(jobs_list) is 0:
        return jsonify(json.loads("[]"))

    json_result="["

    for current in jobs_list:
        current_json = '{"id": "' + current.id + '", "name": "' + current.name + '", "time": "' + str(current.trigger.fields[5]) + ':' + str(current.trigger.fields[6]) + '"},'
        json_result += current_json

    json_result = (json_result[:-1] + ']')

    return jsonify(json.loads(json_result))

@app.route('/add_job')
@roles_required('FULL')
def add_job():
    """Add a job"""
    job_name = request.args.get('job_name')
    hour = request.args.get('hour')
    minute = request.args.get('minute')

    scheduler.add_job(engine.feed, job_name, hour, minute)
    return jsonify(result="")

@app.route('/remove_job')
@roles_required('FULL')
def remove_job():
    """Remove a job"""
    job_id = request.args.get('job_id')
    scheduler.remove_job(job_id)
    return jsonify(result="")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1135, debug=False, threaded=True, ssl_context='adhoc')
