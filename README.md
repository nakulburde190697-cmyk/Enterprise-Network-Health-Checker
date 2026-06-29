# Enterprise Network Health Checker

## Overview

Enterprise Network Health Checker is a Python-based network automation project that evaluates the health of Cisco Nexus switches using predefined health rules.

The application reads device information from a JSON inventory, checks CPU utilization, memory utilization, temperature, and reachability status, then generates both a console health report and a timestamped CSV report.

This project demonstrates Python programming, modular application design, JSON parsing, CSV report generation, and Git version control.

---

## Features

* Reads device inventory from a JSON file
* Evaluates device health using configurable thresholds
* Detects unreachable devices
* Detects CPU and memory threshold violations
* Detects high temperature conditions
* Generates timestamped CSV reports
* Displays a console health summary
* Modular Python architecture

## Technologies Used

* Python 3
* JSON
* CSV
* Git

---

## Project Structure

```text
Enterprise-Network-Health-Checker/
│
├── main.py
├── health_checker.py
├── csv_report.py
├── devices.json
├── README.md
├── .gitignore
└── reports/

## Health Rules

| Parameter            | Status   |
| -------------------- | -------- |
| CPU >= 90%           | CRITICAL |
| CPU >= 75%           | WARNING  |
| Memory >= 90%        | CRITICAL |
| Memory >= 80%        | WARNING  |
| Temperature = High   | CRITICAL |
| Status = Unreachable | DOWN     |

---

## Sample Output

```text
Health Summary

Healthy Devices : 1
Warning Devices : 0
Critical Devices : 1
Down Devices : 1
Total Devices : 3
```

---

## Future Improvements

* Cisco REST API integration
* Netmiko support
* Email alerting
* HTML dashboard
* Multi-device inventory collection
* Logging support

## Author
Nakul Burde
Network Engineer | Python for Network Automation | Cisco Networking