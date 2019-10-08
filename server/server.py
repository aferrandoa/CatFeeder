#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  	server.py
# 	PiCam Local Web Server with Flask

from flask import Flask, render_template, Response, jsonify, url_for
import json

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
import engine
import database
import scheduler

app = Flask(__name__)

@app.route('/')
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
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
					
@app.route('/open_action')
def open_action():
    """Test action url"""
    engine.open_door()
    print("Action done")
    return jsonify(result="")
	
@app.route('/close_action')
def close_action():
    """Test action url"""
    engine.close_door()
    print("Action done")
    return jsonify(result="")

@app.route('/get_jobs')
def get_jobs():
    """Get jobs list"""
    jobs_list = scheduler.get_all_jobs()
    print(jobs_list)

    json_result = {
        "id" : jobs_list[0].id,
        "name": jobs_list[0].name
    }

    return jsonify(json_result)

@app.route('/add_job')
def add_job():
    """Add a job"""
    scheduler.add_job(engine.open_door)
    return jsonify(result="")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False, threaded=True)
