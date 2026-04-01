#!/bin/bash

echo "Deploying application..."

cd /home/ec2-user/app

git pull origin main

pip3 install -r requirements.txt

pkill -f main.py || true

nohup python3 main.py > output.log 2>&1 &

echo "Deployment completed!"