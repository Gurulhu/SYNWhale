version: "3"

# More info at https://github.com/pi-hole/docker-pi-hole/ and https://docs.pi-hole.net/
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "67:67/udp"
      - "80:80/tcp"
      - "443:443/tcp"
    environment:
      TZ: 'America/Sao_Paulo'
      WEBPASSWORD: 'vememefodebebe'
      #Quad9 filtered+DNSSED resolver
      DNS1: '9.9.9.9'
      DNS2: '149.112.112.112'
      DNSSEC: 'True'
    # Volumes store your data between container upgrades
    volumes:
      - './etc/pihole/:/etc/pihole/'
      - './etc/dnsmasq.d/:/etc/dnsmasq.d/'
      - './log/pihole/pihole.log:/var/log/pihole.log'
      - './log/pihole/pihole-FTL.log:/var/log/pihole-FTL.log'
#      - './log/pihole/access.log:/var/log/lighttpd/access.log'
#      - './log/pihole/error.log:/var/log/lighttpd/error.log'
    dns:
      - 127.0.0.1
      - 9.9.9.9
    # Recommended but not required (DHCP needs NET_ADMIN)
    #   https://github.com/pi-hole/docker-pi-hole#note-on-capabilities
    cap_add:
      - NET_ADMIN
    restart: unless-stopped

  snort:
    container_name: snort
    image: snort:latest
    network_mode: host
    environment:
      OINKCODE: <oinkcode>
    volumes:
      - './log/snort/:/var/log/snort/'
      - './etc/snort/:/etc/snort/'
    restart: unless-stopped
    command:
      - 'snort -e /etc/snort/snort.conf -A full -i any'

  splunk:
    container_name: splunk
    image: splunk:latest
    ports:
      - '8000:8000/tcp'
    environment: 
      SPLUNK_PASSWORD: <splunkpassword>
      SPLUNK_START_ARGS: '--accept-license'
    volumes:
      - './log/snort/:/var/log/snort/'
      - './log/pihole/:/var/log/pihole/'
      - './log/jump/:/var/log/jump/'
    restart: unless-stopped
    command:
      - start
     
  jump:
    container_name: jump
    image: jump:latest
    ports:
      - "22:22/tcp"
    volumes:
      - './log/jump/auth.log:/var/log/auth.log'
    restart: unless-stopped
