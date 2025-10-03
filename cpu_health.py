import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 80

def monitor_cpu():
    print("Monitoring CPU usage...\n(Press Ctrl + C to stop)\n")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=5)  # percentage over 1 second
            print(f"current cpu usage is {cpu_usage} at {datetime.now()} is Normal")
            if cpu_usage > CPU_THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            time.sleep(1) 
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred during monitoring: {e}")


monitor_cpu()
