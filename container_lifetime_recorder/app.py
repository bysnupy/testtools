"""
* Application name: Recorder of Pod lifetime
* Description: Recording each phase of the containers in a Pod such like starting/termination of each container and receiving signals
* Author: Daein Park
"""

from flask import Flask
from flask import request
from threading import Thread
import sys,os,time,signal
app = Flask(__name__)


listening_port = 8080
container_name = "default"

if os.environ.get('FLASK_RUN_PORT'):
    listening_port = int(os.environ.get('FLASK_RUN_PORT'))
if os.environ.get('CONTAINER_NAME'):
    container_name = str(os.environ.get('CONTAINER_NAME'))
if os.environ.get('EXIT_FAILURE'):
    sys.exit(1)
if os.environ.get('EXIT_SUCCESS'):
    sys.exit(0)
    
def sig_print(signum, frame):
    print(time.strftime('%H:%M:%S'), ": RECEIVED a signal : ", signal.Signals(signum).name)

catchable_sigs = set(signal.Signals)
for sig in catchable_sigs:
    try:
        signal.signal(sig, sig_print)
    except (ValueError, OSError, RuntimeError) as m:
        pass

print(time.strftime('%H:%M:%S'), ": STARTED, Container name: ", container_name);

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def request_main(req_path):
    return "OK"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=listening_port, debug=True)
