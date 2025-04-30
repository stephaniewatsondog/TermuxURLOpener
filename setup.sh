#!/bin/bash
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
pip install requests beautifulsoup4
termux-wake-lock
nohup python url_opener.py &
