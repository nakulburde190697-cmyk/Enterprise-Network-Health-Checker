import csv
import os
from datetime import datetime
from health_checker import check_health

def generate_csv(devices):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/health_report_{timestamp}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Hostname",
            "Management IP",
            "CPU",
            "Memory",
            "Temperature",
            "Status",
            "Overall Health"
        ])
        for device in devices:
            health = check_health(device)
            writer.writerow([
                device["hostname"],
                device["management_ip"],
                device["cpu"],
                device["memory"],
                device["temperature"],
                device["status"],
                health
            ])
    return filename