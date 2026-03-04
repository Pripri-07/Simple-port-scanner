print("DEBUG: Script started")  # optional debug line

import argparse
from scanner import run_scan   # 👈 THIS LINKS scanner.py


def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")

    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("-sp", "--startport", type=int, required=True, help="Start port")
    parser.add_argument("-ep", "--endport", type=int, required=True, help="End port")
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads")
    parser.add_argument("-b", "--banner", action="store_true", help="Enable banner grabbing")

    args = parser.parse_args()

    run_scan(
        target=args.target,
        start_port=args.startport,
        end_port=args.endport,
        threads=args.threads,
        banner=args.banner
    )


if __name__ == "__main__":
    main()