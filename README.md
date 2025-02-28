# Test tools

Simple applications for testing.

You can build and deploy the applications as follows.

```console
$ oc new-app python~https://github.com/bysnupy/testtools.git \
     --context-dir=<application directory name>
```

 Name | Description | Usecases 
------|-------------|------------
[Httpd connection status recorder](https://github.com/bysnupy/testtools/tree/master/http-conn-recorder) | You can trace the connection status history using /tmp/YYYY-MM-DD_server-status files in the pod. | It's helpful to find out how well their server is performing through concurrent connection counts.
[Datetime recorder for HTTP requests](https://github.com/bysnupy/testtools/tree/master/http-datetime-recorder) | This application for testing up-and-running of the pod while something is changing or trouble is occurred using recorded sequential time record logs for a mean time. | It's helpful to check if which requests can be reached out to the pod or not.
[HTTP Reqeust receiver](https://github.com/bysnupy/testtools/tree/master/http-req-receiver) | This is a simple web server to test any HTTP requests from external | It's helpful to check if external requests can be reached to the pod or not with each of 200 and 500 status codes.
[HTTP Reqeust/Response header debugger](https://github.com/bysnupy/testtools/tree/master/http-show-header) | This is a simple web server to show you any HTTP requests/responses headers | It's helpful to check all header parameters. Specifically, it's useful to troubleshoot for Service Mesh.
[HTTP Slow responsor](https://github.com/bysnupy/testtools/tree/master/http-slow-responsor) | This is a simple web server to test timeout influence for slow responses. | It's helpful to check influence of the long latency of the response at the endpoint pod. 
[Conatainer Lifetime Recorder](https://github.com/bysnupy/testtools/tree/master/container_lifetime_recorder) | Recording time at each phase of the containers in a Pod such like starting/termination of each container and receiving signal | It's helpful to test container starting and termination details

There may be some applications which are implemented with other languages, it's provided a specific usage through README file under its context dir.

[![License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)
