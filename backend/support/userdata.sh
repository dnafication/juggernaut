# /bin/env bash

yum update -y

# install docker
yum install -y docker git python36

# start the service
service docker start

# Add the ec2-user to the docker group so 
# you can execute Docker commands without using sudo.
usermod -a -G docker ec2-user

# pip packages
pip install ansible==2.7
pip install bzt==1.13.0

