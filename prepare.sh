#Configure Docker-Compose
cp docker-compose.yml.spec docker-compose.yml.spec

echo "Paste your oinkcode for snort configuration:"
read OINKCODE
sed -i "s/<oinkcode>/${OINKCODE}/g" docker-compose.yml

echo "Type the administrator password for your splunk instance:"
read SPLUNK_PASSWORD
sed -i "s/<splunkpassword>/${SPLUNK_PASSWORD}/g" docker-compose.yml

#Create log files to avoid mounting issues:

mkdir -p ./log/pihole
touch ./log/pihole/pihole.log
touch ./log/pihole/pihole-FTL.log
touch ./log/pihole/access.log
touch ./log/pihole/error.log

mkdir -p ./log/snort

mkdir -p ./log/jump
touch ./log/jump/auth.log

#Compile images (this takes time. A lot of time.)
docker build -t jump ./images/jump/
docker build -t snort ./images/snort/
docker build -t splunk ./images/splunk/

echo "Done! Now run docker-compose up to fire it all up."
