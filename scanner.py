import socket
import threading
from queue import Queue


def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print("[-] Unable to resolve target.")
        exit()


def scan_port(ip, port, banner=False):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

            if banner:
                try:
                    banner_data = s.recv(1024).decode().strip()
                    if banner_data:
                        print(f"    Banner: {banner_data}")
                except:
                    pass

        s.close()

    except:
        pass


def worker(ip, banner, queue):
    while not queue.empty():
        port = queue.get()
        scan_port(ip, port, banner)
        queue.task_done()


def run_scan(target, start_port, end_port, threads=50, banner=False):
    ip = resolve_target(target)

    print("=" * 60)
    print("        SIMPLE PORT SCANNER (Educational)")
    print("=" * 60)
    print(f"[+] Target: {target} ({ip})")
    print(f"[+] Port Range: {start_port}-{end_port}")
    print(f"[+] Threads: {threads}")
    print("[+] Starting scan...\n")

    queue = Queue()

    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(threads):
        t = threading.Thread(target=worker, args=(ip, banner, queue))
        t.daemon = True
        t.start()

    queue.join()

    print("\n[+] Scan Complete.")