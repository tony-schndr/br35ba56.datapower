FROM ibmcom/datapower
ENV DATAPOWER_ACCEPT_LICENSE="true" 
ENV DATAPOWER_INTERACTIVE="true" 
EXPOSE 9090
EXPOSE 5554
EXPOSE 8443
VOLUME ["/opt/ibm/datapower/drouter/config", "/opt/ibm/datapower/drouter/local", "/opt/ibm/datapower/root/secure/usrcerts"]

USER root
RUN chown -R drouter:drouter /opt/ibm/datapower/drouter/config \
                             /opt/ibm/datapower/drouter/local \
                             /opt/ibm/datapower/root/secure/usrcerts
RUN set-user drouter
USER drouter