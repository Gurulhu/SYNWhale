#!/bin/bash

service rsyslog restart
service ssh restart

#Keeps the container running:
tail -f /dev/null  
