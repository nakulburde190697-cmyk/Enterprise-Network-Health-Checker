import json
from csv_report import generate_csv
from health_checker import check_health
with open("devices.json", "r") as file:
    data_dict = json.load(file)
    devices = data_dict["devices"]
    summary = {
    "Healthy": 0,
    "WARNING": 0,
    "CRITICAL": 0,
    "DOWN": 0
}
    for device in devices:
        health = check_health(device)
        summary[health] += 1
        print("=" * 50)
        print(f"Hostname      : {device['hostname']}")
        print(f"Management IP : {device['management_ip']}")
        print(f"CPU           : {device['cpu']}")
        print(f"Memory        : {device['memory']}")
        print(f"Temperature   : {device['temperature']}")
        print(f"Status        : {device['status']}")
        print(f"Overall Health: {health}")
        print("=" * 50)
    report_file = generate_csv(devices)
    print("\n" + "=" * 50)
print("Health Summary")
print("=" * 50)
print(f"Healthy Devices  : {summary['Healthy']}")
print(f"Warning Devices  : {summary['WARNING']}")
print(f"Critical Devices : {summary['CRITICAL']}")
print(f"Down Devices     : {summary['DOWN']}")
print(f"Total Devices    : {len(devices)}")
print("=" * 50)
print("\nCSV report generated successfully!")
print(f"CSV Report Saved : {report_file}")

