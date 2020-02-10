# S.Y.N. Whale

### A dockerized gateway to secure your home network.

## The Framework

The goal of this project is to provide a simple script anyone can run to setup a basic network inspection/monitoring environment.
It accomplishes this goal by using a handful of tools to secure and monitor the traffic going in and out.
Those tools, along with their respective functions, are:

* Pi-hole: 
  DNS Sinkhole that acts as a network-wide ad blocker. 
  It also serves as DHCP, but that's currently a WIP for this project.
  Collects both DNS Query and DHCP logs.

* Snort:
  Network IDS with IPS capabilities in the right setup.
  Comes packed with latest snapshot (but requires an Oinkcode) and can raise alerts and log the pcap for the detected communication.
  
* Splunk:
  Free version of the famous proprietary SIEM. 
  Helps in the aggregation and visualization of all the data collected.
  Provides statistics and insight.

* Squid:
  Free, transparent proxy.
  Doesn't provide "security" and it's optional for network users, but can speed browsing experience with it's cache functionality.
  Provides us web logs, gathering more context than raw DNS logs.

* Jumpserver:
  A hardened container to be exposed as your ssh entrypoint.
  Provides an standartized entrypoint from where you can jump into other boxes.
  Help with whitelisting and firewall management, being a sole point of access.
  Have a fail2ban framework configured to keep lazy/known scans and bruteforcers out.
  Provides fail2ban alerts and SSH connection logs.

## Where we are

This project is currently a work in progress and can be considered, if much, an alpha version for now.
The status of each container is as follows:
* Pi-hole:
  * DNS filter and logging working.
  * Lacks custom filterlists and jumpserver's fail2ban integration.
  * DHCP function is not yet enabled/configured.
* Snort:
  * Acting on detection mode.
  * No custom rules.
  * No periodic updates enabled.
* Splunk:
  * Log collection is working.
  * No premade dashboards.
  * Timezone issues.
* Squid:
  * Not yet installed.
* Jumpserver:
  * Currently on sprint.
  * Not yet hardened.

## Roadmap

The roadmap described bellow is drafted roughly by urgency, so point orders may change.

//Create and configure the remaining tools
* Configure the jumpserver
* Harden the jumpserver
* Configure squid
* Mount Splunk logs outside the image
//Glue the pieces/integrate
* Fix the ntp/timezone across containers
* Configure the pihole DHCP
* Serve proxy and dns configurations via DHCP
* Integrate fail2ban banlist with pihole's, squid's and snort's 
//Improvements and enrichments
* Create basic splunk dashboards for provided tools
* Create custom rules
//Long-run possibilities and evil plans
* Unify the data gathered into a custom banlist
* Create custom rules to be shared
* Implement some form of user control (maybe LDAP?)
* Implement basic asset discover (Can be done with DHCP and DNS, but a ping sweep for service discover sounds nice)

