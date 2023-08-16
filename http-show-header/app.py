"""
* Application name: HTTP Reqeust/Response header debugger
* Description: This is a simple web server to show you any HTTP requests/responses headers
* Author: Daein Park
"""

from flask import Flask
from flask import request
import os,time
app = Flask(__name__)


listening_port = 8080
if os.environ.get('FLASK_RUN_PORT'):
    listening_port = int(os.environ.get('FLASK_RUN_PORT'))

print("Start time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def request_main(req_path):
    print("--- Request HEADER start")
    print(request.headers)
    return 'OK'

@app.after_request
def after_request(response):
    print("--- Response HEADER start")
    print(response.headers)
    return response

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=listening_port, debug=True)
