#!/bin/bash

python3 -m venv rosterapp-venv
source rosterapp-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py