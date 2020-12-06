FROM quay.io/fedora/fedora:34-x86_64

ENV HTTPD_STREAM=2.4

ENV SUMMARY="httpd web server for checking connection status using server-status handler." \
    DESCRIPTION="You can trace the connection status history using /tmp/YYYY-MM-DD_server-status files."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Apache httpd $HTTPD_STREAM for checking connection status" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="httpd,httpd-24" \
      name="http-conn-recorder" \
      version="1" \
      maintainer="Daein Park"

EXPOSE 8080

RUN yum -y module enable httpd:$HTTPD_STREAM && \
    INSTALL_PKGS="hostname elinks bind-utils nss_wrapper gettext iproute iputils wget httpd" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum -y clean all --enablerepo='*'

ENV HTTPD_WRAPPER_PATH=/usr/bin \
    HTTPD_CONFIGURATION_PATH=/etc/httpd \
    HTTPD_MAIN_CONF_PATH=/etc/httpd/conf \
    HTTPD_MAIN_CONF_D_PATH=/etc/httpd/conf.d \
    HTTPD_VAR_RUN=/var/run/httpd \
    HTTPD_DATA_PATH=/var/www \
    HTTPD_DATA_ORIG_PATH=/var/www \
    HTTPD_LOG_PATH=/var/log/httpd

COPY ./conf.d/  $HTTPD_MAIN_CONF_D_PATH
COPY ./bin/     $HTTPD_WRAPPER_PATH
COPY ./workdir/ /tmp

RUN  /usr/bin/chmod a+x /usr/bin/run-httpd && \
     /usr/bin/chmod -R a+rwx ${HTTPD_MAIN_CONF_PATH} && \
     /usr/bin/chmod -R a+rwx ${HTTPD_MAIN_CONF_D_PATH} && \
     /usr/bin/chmod -R a+rwx ${HTTPD_VAR_RUN} && \
     /usr/bin/chown -R 1001:0 ${HTTPD_DATA_PATH} && \
     /usr/bin/chmod -R g+rwx ${HTTPD_LOG_PATH} && \
     /usr/bin/chown -R 1001:0 ${HTTPD_LOG_PATH} && \
     /usr/bin/sed -i -e "s/^User apache/User default/" ${HTTPD_MAIN_CONF_PATH}/httpd.conf && \
     /usr/bin/sed -i -e "s/^Group apache/Group root/" ${HTTPD_MAIN_CONF_PATH}/httpd.conf && \
     /usr/bin/sed -ri 's!^(\s*CustomLog)\s+\S+!\1 |/usr/bin/cat!g; s!^(\s*ErrorLog)\s+\S+!\1 |/usr/bin/cat!g;' ${HTTPD_MAIN_CONF_PATH}/httpd.conf && \
     /usr/bin/sed -i -e 's/^Listen 80/Listen 0.0.0.0:8080/' ${HTTPD_MAIN_CONF_PATH}/httpd.conf && \
     /usr/bin/sed -i -e 's/localhost:80/localhost:8080/g' /usr/sbin/apachectl

USER 1001

CMD ["/usr/bin/run-httpd"]
