#Hardened SSH Jumpserver
FROM ubuntu:latest

MAINTAINER Gurulhu <lucasag@hotmail.com.br>

RUN apt-get update && \
    apt-get install -y \
    ssh \
    fail2ban \
    rsyslog

#Set a few log options so we can fail2ban the shit off
RUN sed -i "s/#SyslogFacility AUTH/SyslogFacility AUTH/g" /etc/ssh/sshd_config \
    && sed -i "s/#LogLevel INFO/LogLevel VERBOSE/g" /etc/ssh/sshd_config

RUN useradd -m landing

WORKDIR /home/landing

RUN touch /var/log/auth.log

COPY docker-entrypoint.sh /home/landing/docker-entrypoint.sh
RUN chmod 700 /home/landing/docker-entrypoint.sh

ENTRYPOINT ["/home/landing/docker-entrypoint.sh"]
