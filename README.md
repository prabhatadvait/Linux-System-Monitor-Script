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
linux-system-monitor/ │ ├── system_monitor.py # Main script ├── system_monitor.log # Log file (generated after running the script) └── README.md # Documentation

bash
Copy
Edit

## **🚀 Quick Start**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/linux-system-monitor.git
cd linux-system-monitor
Step 2: Install Dependencies
Make sure Python is installed (version 3.6+). Install the psutil library using:

bash
Copy
Edit
pip install psutil
Step 3: Run the Script
Make the script executable:

bash
Copy
Edit
chmod +x system_monitor.py
Run the script:

bash
Copy
Edit
./system_monitor.py
Step 4: View Logs
The script logs system stats into system_monitor.log. Check it with:

bash
Copy
Edit
cat system_monitor.log
📸 Sample Output
Real-Time Monitoring (Terminal)
plaintext
Copy
Edit
Linux System Monitor
Press Ctrl+C to exit.

Time: 2025-01-20 14:30:45
CPU Usage: 15.6%
Memory Usage: 62.4%
Disk Usage: 44.1%
Log File (system_monitor.log)
plaintext
Copy
Edit
2025-01-20 14:30:45: CPU: 15.6%, Memory: 62.4%, Disk: 44.1%
2025-01-20 14:30:50: CPU: 18.3%, Memory: 63.0%, Disk: 44.2%
⚙️ Customization
Update Interval
Change the update frequency by modifying the time.sleep(5) line in the script:

python
Copy
Edit
time.sleep(10)  # Update every 10 seconds
Add Metrics
You can add features like network monitoring or battery status. For example:

python
Copy
Edit
net_io = psutil.net_io_counters()
print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")
📜 Prerequisites
🐧 Linux-based system
🐍 Python 3.6+
📦 psutil: Install using pip install psutil.
💡 Why Showcase This Project?
This project highlights your:

Linux proficiency.
Scripting skills with Python.
Ability to use tools like psutil.
Practical knowledge of system monitoring and logging.
🛠 Tools Used
Programming Language: Python
Libraries: psutil
Platform: Linux
Terminal Customization: Bash/CLI commands
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repo.
Create a feature branch: git checkout -b feature-name.
Submit a pull request.
📞 Contact
Feel free to connect with me:

LinkedIn: Prabhat Sharma
Portfolio: Portfolio Website
GitHub: PrabhatAdvait
🌟 Show Your Support
If you like this project, don’t forget to give it a ⭐️ on GitHub.
