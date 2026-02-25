import socket
import sys
import threading
from datetime import datetime


def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print("Unable to resolve hostname.")
        sys.exit()


def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode().strip()
                if banner == "":
                    banner = "Unknown Service"
            except:
                banner = "Unknown Service"

            print(f"[OPEN] Port {port} | Service: {banner}")

        s.close()

    except:
        pass


def main():
    if len(sys.argv) != 4:
        print("Usage: python simple_threaded_scanner.py <target> <start_port> <end_port>")
        sys.exit()

    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    target_ip = resolve_target(target)

    print("-" * 50)
    print(f"Scanning Target: {target} ({target_ip})")
    print(f"Port Range: {start_port} - {end_port}")
    print("Started at:", datetime.now())
    print("-" * 50)

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("-" * 50)
    print("Scanning Completed at:", datetime.now())
    print("-" * 50)


if __name__ == "__main__":
    main()