"""
* Application name: HTTP Slow responsor
* Description: This is a simple web server to test any HTTP slow response for timeout influence test
* Logs format: You can identify a certain request using session id
  e.g.> it's one set per one request
                      | session id                       |
  2020-10-09 14:21:26 : 6ac615977b0f0eeec218d8c22fc89f93 : configured timeout: 60
  2020-10-09 14:22:26 : 6ac615977b0f0eeec218d8c22fc89f93 : configured timeout: 60 : real elapsed time: 60.0598750114
  127.0.0.1 - - [09/Oct/2020 14:22:26] "GET /test HTTP/1.1" 200 -
* Author: Daein Park
* Options for changing timeout values
  - when server starts, you can configure initialization of the time out using INIT_TIMEOUT
  - you can also change the timeout using '?timeout=XX' dynamically.
"""

from flask import Flask
from flask import request
import os,time,uuid,hashlib
app = Flask(__name__)

timeout = 60
if os.environ.get('INIT_TIMEOUT'):
    timeout = int(os.environ.get('INIT_TIMEOUT'))

print("Server start time: ", time.strftime('%A %B, %d %Y %H:%M:%S'));

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def request_main(req_path):
    global timeout

    # specify the timeout using 'timeout' query string.
    if request.args.get('timeout'):
        timeout = int(request.args.get('timeout'))

    session_id = hashlib.md5(str(uuid.uuid4()).encode('utf-8')).hexdigest()

    print("%s : %s : configured timeout: %s" % (time.strftime('%Y-%m-%d %H:%M:%S'), session_id, str(timeout)))
    start_time = time.time()
    time.sleep(timeout)
    print('%s : %s : configured timeout: %s : real elapsed time: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), session_id, str(timeout), time.time()-start_time))

    return 'OK, session id: %s' % (session_id)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)
