import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print("-" * 40)

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")

            s.close()

        except KeyboardInterrupt:
            print("\nScanning stopped by user.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break

    print("\nScanning completed.")


# ===== Main Program =====
if __name__ == "__main__":
    target_ip = input("Enter target IP address (e.g., 127.0.0.1): ")
    start = int(input("Enter starting port: "))
    end = int(input("Enter ending port: "))

    scan_ports(target_ip, start, end)