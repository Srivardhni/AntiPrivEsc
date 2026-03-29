SUSPICIOUS_KEYWORDS = ["cmd.exe", "powershell", "bash", "netcat"]

def detect_suspicious(processes):
    alerts = []
    for proc in processes:
        name = proc.get("name", "").lower()
        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword in name:
                alerts.append(proc)
    return alerts