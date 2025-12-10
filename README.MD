# DevOps Infrastructure Provisioning & Configuration Project

# Overview
The project simulates creating virtual machines checking the input, saving it to a JSON file
and running simple Bash scripts to install things like Nginx and Pydantic Automatically
if nginx & pydantic are installed they will notify you (works only in bash environment)


# Objectives
Let the user create VM configs (name, OS, CPU, RAM)
Validate the input using Python and Pydantic
Save all VM configs into a JSON file
Run Bash scripts from Python using subprocess
Write logs to a file so I can see what happened in the run

# Setup
Run the project from a Bash-compatible terminal (Linux / WSL / Git Bash)
(Optional) activate your Python venv before running

# How to run
From the project root
python src/infra_simulator.py
(or just press play)


(Example expected output)

starting the program . . .
enter machine name: ASAF
Operating System (ubuntu, centos, windows): ubuntu
CPU cores (number): 12
RAM size (GB): 24
Machine saved successfully
ended the program