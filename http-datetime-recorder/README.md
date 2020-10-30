# datetime recorder web server

# Descriptions
This application for testing up-and-running of the pod while something is changing or trouble is occurred using recorded sequential time record logs for a mean time.

# Usage
```
$ oc new-app golang~https://github.com/bysnupy/testtools.git \
     --context-dir=http-datetime-recorder
$ oc expose deployment/testtools --port 8080
$ oc expose svc testtools
```
