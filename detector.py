import psutil
import time

def detect_reverse_shell():
    print("[*] Scanning active connections...")
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.raddr:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}"
            print(f"[!] Potential reverse shell: {laddr} <--> {raddr}")

print("[*] Reverse Shell Detector Started. Press Ctrl+C to stop.")
try:
    while True:
        detect_reverse_shell()
        time.sleep(3)
except KeyboardInterrupt:
    print("\n[*] Stopped monitoring.")
