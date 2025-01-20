# **🔧 Linux System Monitor Script**

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Terminal](https://img.shields.io/badge/Terminal-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)  

A lightweight, Python-based script to monitor system performance in real-time on **Linux systems**. Perfect for developers and sysadmins to gain quick insights into CPU, memory, and disk usage. 📊  

## **✨ Features**
- 🖥️ Real-time monitoring of **CPU, Memory, and Disk usage**.  
- 📝 **Logs data** into a file for further analysis.  
- ⚡ Lightweight and efficient script with minimal dependencies.  
- 💻 Designed for Linux systems but works cross-platform.  

## **📂 Project Structure**
bash
linux-system-monitor/
│
├── system_monitor.py # Main script
├── system_monitor.log # Log file (generated after running the script)
└── README.md # Documentation

## **🚀 Quick Start**
Step 1: Clone the Repository

git clone https://github.com/prabhatadvait/Linux-System-Monitor-Script.git
cd Linux-System-Monitor-Script

Step 2: Install Dependencies
Make sure Python is installed (version 3.6+). Install the psutil library using:
pip install psutil

Step 3: Run the Script
Make the script executable:
chmod +x system_monitor.py
Run the script:
./system_monitor.py

Step 4: View Logs
The script logs system stats into system_monitor.log. Check it with:
cat system_monitor.log

## **📸 Sample Output**
Real-Time Monitoring (Terminal)

Linux System Monitor
Press Ctrl+C to exit.

Time: 2025-01-20 12:30:00
CPU Usage: 23%
Memory Usage: 56%
Disk Usage: 65%
