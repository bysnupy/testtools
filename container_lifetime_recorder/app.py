"""
* Application name: Recorder of Pod lifetime
* Description: Recording each phase of the containers in a Pod such like starting/termination of each container and receiving signals
* Author: Daein Park
"""

import sys,os,time,signal
from datetime import datetime

container_name = "default"
exit_timeout = 0

if os.environ.get('CONTAINER_NAME'):
    container_name = str(os.environ.get('CONTAINER_NAME'))
if os.environ.get('EXIT_TIMEOUT'):
    exit_timeout = int(os.environ.get('EXIT_TIMEOUT'))

def sig_print(signum, frame):
    print(datetime.now().strftime('%T.%f')[:-3], ":", container_name, ": RECEIVED a signal : ", signal.Signals(signum).name)
    time.sleep(exit_timeout)
    print(datetime.now().strftime('%T.%f')[:-3], ":", container_name, ": TERMINATED after", exit_timeout, "seconds since received", signal.Signals(signum).name)
    sys.exit(0)

catchable_sigs = set(signal.Signals)
for sig in catchable_sigs:
    try:
        signal.signal(sig, sig_print)
    except (ValueError, OSError, RuntimeError) as m:
        pass

print(datetime.now().strftime('%T.%f')[:-3], ":", container_name, ": STARTED")
if os.environ.get('EXIT_FAILURE'):
    print(datetime.now().strftime('%T.%f')[:-3], ":", container_name, ": STOPPED with 1 exit code")
    sys.exit(1)
if os.environ.get('EXIT_SUCCESS'):
    print(datetime.now().strftime('%T.%f')[:-3], ":", container_name, ": STOPPED with 0 exit code")
    sys.exit(0)

time.sleep(36000)
sys.exit(0)
