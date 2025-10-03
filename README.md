**
Assignment Title - DevOps Automation with Python – Script Collection

Description

This repository contains solutions to a set of DevOps-focused Python automation tasks. These scripts demonstrate core DevOps practices such as:

Security (Password Strength Checker)

System Monitoring (CPU Health Monitor)

Backup Automation (File Backup with Timestamps)

Each script handles real-world scenarios and includes robust error handling to simulate production-readiness.

Questions Attempted
Q1: Password Strength Checker

A Python script that evaluates the strength of a user-provided password based on:

Minimum length (8 characters)

Includes uppercase and lowercase letters

At least one digit

At least one special character (!@#$% etc.)

Files:

password_checker.py

How to Run:

python password_checker.py


Sample Output:

Enter password: MyPass@123
Password is strong

🖥️ Q2: CPU Health Monitor

A Python script that continuously monitors CPU usage. If usage exceeds 80%, an alert is displayed. Runs until manually interrupted.

Libraries Used: psutil

Files:

cpu_monitor.py

How to Run:

pip install psutil
python cpu_monitor.py


Sample Output:

Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
...

💾 Q4: Backup Script

A command-line script to back up files from a source directory to a destination. If a file with the same name exists in the destination, a timestamp is added to avoid overwriting.

Files:

backup.py

How to Run:

python backup.py /path/to/source /path/to/destination


Example:
If report.txt already exists, a backup like report_20251003_153025.txt will be created.

Environment & Tools

Python 3.x

Standard Python libraries (os, sys, shutil, datetime, re)

Optional: psutil for CPU monitoring

💡 How to Set Up the Project

Clone the repo:

git clone https://github.com/saiyedin786/python_assignment
cd devops-python-assignment


Run the scripts using instructions in each section.

Submission Details

Submitted by: Ismail saiyed

Course: Python for Devops

Instructor: Prashant

Submission Platform: Vlearn

Repository Link: GitHub Repo



**
