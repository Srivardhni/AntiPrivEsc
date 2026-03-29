from monitor.process_monitor import get_running_processes
from core.detector import detect_suspicious
from core.logger import log_alert

def run():
    processes = get_running_processes()
    alerts = detect_suspicious(processes)

    for alert in alerts:
        print(f"[⚠️] Suspicious Process: {alert}")
        log_alert(alert)

if __name__ == "__main__":
    run()