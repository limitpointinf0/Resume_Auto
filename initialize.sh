#!/bin/sh

python3 helpers/run.py & 
~/Desktop/ngrok http 5000 & 

wait