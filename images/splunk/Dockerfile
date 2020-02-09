#SplunkForwarder but configured for this project.
FROM splunk/splunk:latest

MAINTAINER Gurulhu <lucasag@hotmail.com.br>

RUN sudo chown ansible -R /var/log \
    && mkdir -p /var/log/pihole \
    && mkdir -p /var/log/snort \
    && mkdir -p /var/log/jump \ 
    && touch /var/log/pihole/pihole.log \
    && touch /var/log/pihole/pihole-FTL.log \
    && touch /var/log/snort/alert \
    && touch /var/log/jump/auth.log

COPY inputs.conf /opt/splunk/etc/system/local/
#COPY outputs.conf /opt/splunk/etc/system/local/
