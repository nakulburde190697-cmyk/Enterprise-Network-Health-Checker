def check_health(device):
    if device["status"] == "Unreachable":
        return "DOWN"
    if device["temperature"] == "High":
        return "CRITICAL"
    if device["cpu"] >= 90:
        return "CRITICAL"
    if device["memory"] >= 90:
        return "CRITICAL"
    if device["cpu"] >= 75:
        return "WARNING"
    if device["memory"] >= 80:
        return "WARNING"
    return "Healthy"