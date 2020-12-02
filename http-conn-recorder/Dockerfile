FROM registry.redhat.io/rhel8/httpd-24

USER 0

RUN yum install -y --setopt=tsflags=nodocs yum-utils iputils iproute nmap-ncat && \
    yum-config-manager --enable codeready-builder-for-rhel-8-x86_64-rpms && \
    yum install -y --setopt=tsflags=nodocs elinks && \
    yum -y clean all --enablerepo='*'

COPY ./conf.d/ $HTTPD_MAIN_CONF_D_PATH/
COPY ./bin/    /usr/bin/

RUN  /usr/bin/chmod a+x /usr/bin/run-httpd && \
     /usr/bin/sed -i -e 's/localhost:80/localhost:8080/g' /usr/sbin/apachectl && \
     /usr/libexec/httpd-prepare && rpm-file-permissions

USER 1001
