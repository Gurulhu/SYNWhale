# Snort in Docker
FROM ubuntu:latest

MAINTAINER John Lin <linton.tw@gmail.com> (Forked from)
MAINTAINER Gurulhu <lucasag@hotmail.com.br>

RUN apt-get update && \
    apt-get install -y \
        python-setuptools \
        python-pip \
        python-dev \
        wget \
        build-essential \
        bison \
        flex \
        libpcap-dev \
        libpcre3-dev \
        libdumbnet-dev \
        zlib1g-dev \
        iptables-dev \
        libnetfilter-queue1 \
        tcpdump \
        unzip \
        git \
        perl \
        libssl-dev \
        libwww-perl \
        vim && pip install -U pip dpkt snortunsock

# Define working directory.
WORKDIR /opt

ENV DAQ_VERSION 2.0.6
RUN wget https://www.snort.org/downloads/snort/daq-${DAQ_VERSION}.tar.gz \
    && tar xvfz daq-${DAQ_VERSION}.tar.gz \
    && cd daq-${DAQ_VERSION} \
    && ./configure; make; make install

ENV SNORT_VERSION 2.9.15.1
RUN wget https://www.snort.org/downloads/snort/snort-${SNORT_VERSION}.tar.gz \
    && tar xvfz snort-${SNORT_VERSION}.tar.gz \
    && cd snort-${SNORT_VERSION} \
    && ./configure --disable-open-appid --enable-non-ether-decoders --enable-sourcefire; make; make install 

RUN ldconfig

# ENV SNORT_RULES_SNAPSHOT 2972
# ADD snortrules-snapshot-${SNORT_RULES_SNAPSHOT} /opt
#ADD mysnortrules /opt
RUN mkdir -p /var/log/snort \
    && mkdir -p /usr/local/lib/snort_dynamicrules \
    && mkdir -p /etc/snort \
    && mkdir -p /etc/snort/rules \
    # && mkdir -p /etc/snort/preproc_rules \
    # && mkdir -p /etc/snort/so_rules \
    # && mkdir -p /etc/snort/etc \

    #Download configuration files \
    && wget https://www.snort.org/documents/classification-config -O /etc/snort/classification.config \
    && wget https://www.snort.org/documents/reference-config -O /etc/snort/reference.config 

    # && touch /etc/snort/rules/local.rules \
    # && touch /etc/snort/rules/white_list.rules /etc/snort/rules/black_list.rules

#Install pulledpork because managing snork configurations sucks

RUN git clone https://github.com/shirkdog/pulledpork \
    && cd pulledpork/ \
    && cp etc/pulledpork.conf etc/pulledpork.conf.bkp 
    
#RUN cd pulledpork/ \
#    && sed "s/<oinkcode>/"${OINKCODE}"/g" etc/pulledpork.conf.bkp > etc/pulledpork.conf \
#    && mkdir -p /usr/local/etc/snort/rules/iplists \
#    && ./pulledpork.pl -c etc/pulledpork.conf -g\
#    && tar xzf /tmp/snortrules-snapshot*.tar.gz -C /etc/snort/ \
#    && cp /etc/snort/etc/snort.conf /etc/snort/etc/snort.conf.bkp \
#    && sed "s/decompress_swf/#decompress_swf/g" /etc/snort/etc/snort.conf.bkp > /etc/snort/etc/snort.conf

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    /opt/snort-${SNORT_VERSION}.tar.gz /opt/daq-${DAQ_VERSION}.tar.gz

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s /usr/local/bin/docker-entrypoint.sh 

ENV NETWORK_INTERFACE eth0
# Validate an installation
# snort -T -i eth0 -c /etc/snort/etc/snort.conf
CMD ["snort", "-T", "-i", "echo ${NETWORK_INTERFACE}", "-c", "/etc/snort/etc/snort.conf"]

ENTRYPOINT ["docker-entrypoint.sh"]
