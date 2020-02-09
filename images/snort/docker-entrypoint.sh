#!/bin/bash

if [ ! -z "$OINKCODE" ]; then
cd /opt/pulledpork;
cp etc/pulledpork.conf etc/pulledpork.conf.bkp;
sed "s/<oinkcode>/"${OINKCODE}"/g" etc/pulledpork.conf.bkp > etc/pulledpork.conf;
mkdir -p /usr/local/etc/snort/rules/iplists;
./pulledpork.pl -c etc/pulledpork.conf -g;
tar xzf /tmp/snortrules-snapshot*.tar.gz -C /etc/snort/;
cp /etc/snort/etc/snort.conf /etc/snort/etc/snort.conf.bkp;
sed "s/decompress_swf/#decompress_swf/g" /etc/snort/etc/snort.conf.bkp > /etc/snort/etc/snort.conf;
snort -c /etc/snort/etc/snort.conf -A full -i any;
else echo "ERROR: OINKCODE not set.";
fi



/bin/bash
