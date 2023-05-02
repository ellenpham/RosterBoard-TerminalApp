#!/bin/bash

# check if python is installed
python3 -m venv rosterapp-venv

# check if venv already exists
source venv rosterapp-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 src/main.py