#!/bin/sh

python3 run.py & 
~/Desktop/ngrok http 5000 & 

wait
