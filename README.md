# 🔍 Simple Port Scanner

A multithreaded CLI-based Network Reconnaissance Tool built in Python.

This tool attempts to connect to a range of ports on a target IP address or domain name to determine which services are running. It mimics the basic functionality of professional tools like Nmap.

---

## 📌 Features

- Target Parsing (IP address or domain name)
- Automatic Domain → IP Resolution
- Custom Port Range Scanning (e.g., 1–1024 or 1–65535)
- Multithreaded Scanning for Speed
- Optional Service Banner Grabbing
- Adjustable Thread Count
- Adjustable Timeout

---

## 🛠 Tech Stack

- Language: Python 3
- Libraries Used:
  - socket (core networking)
  - threading (parallel scanning)
  - argparse (CLI argument parsing)
  - sys (system interaction)

No external dependencies required.

---

## 📂 Project Structure
simple-port-scanner/
│
├── scanner.py # Core scanning logic
├── main.py # CLI interface
├── requirements.txt
└── README.md

---

## 🚀 Installation

1. Clone the repository:    
    git clone https://github.com/Pripri-07/Simple-port-scanner.git
2. Navigate into the folder:
    cd simple-port-scanner
3. Run the scanner:
    python main.py -t <target> -sp <start_port> -ep <end_port>
---

## 🧪 Usage Examples

### Basic Scan
python main.py -t scanme.nmap.org -sp 1 -ep 100

### Scan with Banner Grabbing
python main.py -t scanme.nmap.org -sp 1 -ep 100 -b

### Scan with Custom Threads and Timeout
python main.py -t 192.168.1.1 -sp 1 -ep 1024 -th 100 -to 0.5

---

## ⚙️ CLI Arguments

| Argument | Description |
|----------|-------------|
| -t / --target | Target IP address or domain name |
| -sp / --start-port | Starting port number |
| -ep / --end-port | Ending port number |
| -th / --threads | Number of threads (default: 50) |
| -to / --timeout | Timeout per port in seconds (default: 1) |
| -b / --banner | Enable service banner grabbing |

---

## 🔎 Example Output
============================================================
SIMPLE PORT SCANNER (Educational)

[+] Target: scanme.nmap.org (45.xx.xx.xx)
[+] Port Range: 1-100
[+] Starting scan...

[+] Open Ports Found:

Port 22 is OPEN
Banner: SSH-2.0-OpenSSH_8.2

Port 80 is OPEN

[+] Scan Complete.

---

## ⚠️ Disclaimer

This tool is intended for educational purposes only.

Do NOT scan systems, networks, or devices without proper authorization.

Unauthorized scanning may violate laws and regulations.

---

## 🎯 Learning Outcomes

This project demonstrates understanding of:

- Socket programming
- TCP connections
- Multithreading in Python
- CLI argument parsing
- Network reconnaissance fundamentals
- Ethical cybersecurity practices

---

## 📈 Future Improvements

- Colored CLI output
- Save results to file
- Progress percentage display
- Service detection improvements
- Packaging as installable CLI tool

---

## 👩‍💻 Author

Built as a beginner cybersecurity project to understand how port scanners work internally.
