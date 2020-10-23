"""
* Application name: HTTP Reqeust receiver
* Description: This is a simple web server to test any HTTP requests from external
* Author: Daein Park
* Options for query string:
  - change the response code 500 using "fail=true", to revert it using "fail=false"
  - when server starts, you can change the response code 500 using "INIT_FAIL=True" env
  - you can change the listening port using "FLASK_RUN_PORT=XXXX" env
"""

from flask import Flask
from flask import request
import os,time
app = Flask(__name__)

fail_flag = False
if os.environ.get('INIT_FAIL') == 'True':
    fail_flag = True

listening_port = 8080
if os.environ.get('FLASK_RUN_PORT'):
    listening_port = int(os.environ.get('FLASK_RUN_PORT'))

print("Start time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def request_main(req_path):
    global fail_flag
    
    # Condition blocks for checking a "fail" query string is true or false
    if request.args.get('fail') == 'true':
        fail_flag = True
    elif request.args.get('fail') == 'false':
        fail_flag = False
    
    # Condition block for response the 500 status code
    if fail_flag:
        raise Exception()
    return 'OK'

@app.errorhandler(Exception)
def failure_error(e):
    return 'You can revert using fail=false query string', 500

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=listening_port, debug=True)
