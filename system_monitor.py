#!/usr/bin/env python3

import os
import psutil
import time
from datetime import datetime

# Function to clear the terminal
def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

# Function to get system stats
def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    return {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage,
    }

# Function to log stats to a file
def log_stats(stats):
    with open("system_monitor.log", "a") as log_file:
        log_file.write(f"{datetime.now()}: CPU: {stats['cpu']}%, Memory: {stats['memory']}%, Disk: {stats['disk']}%\n")

# Main function
def main():
    print("Linux System Monitor")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            clear_terminal()
            stats = get_system_stats()

            print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"CPU Usage: {stats['cpu']}%")
            print(f"Memory Usage: {stats['memory']}%")
            print(f"Disk Usage: {stats['disk']}%")

            log_stats(stats)
            time.sleep(5)  # Update every 5 seconds
    except KeyboardInterrupt:
        print("\nExiting System Monitor.")

if __name__ == "__main__":
    main()
