# /bin/env bash

yum update -y

# install docker et al
yum install -y docker git python36

# install docker compose
curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

docker-compose --version


# start the service
service docker start

# Add the ec2-user to the docker group so 
# you can execute Docker commands without using sudo.
usermod -a -G docker ec2-user

# pip packages
pip install ansible==2.7
pip install bzt==1.13.0

