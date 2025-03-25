import argparse
from sentinel.monitor import monitor_api
from sentinel.load_test import load_test_api

def main():
    parser = argparse.ArgumentParser(prog="Sentinel", description="API Monitoring & Load Testing CLI Tool")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Monitor command
    monitor_parser = subparsers.add_parser("monitor", help="Monitor an API endpoint")
    monitor_parser.add_argument("url", help="API URL to monitor")
    monitor_parser.add_argument("--interval", type=int, default=0, help="Monitoring interval")
    monitor_parser.add_argument("--count", type=int, default=1, help="Stop monitoring after N intervals")

    # Load Test command
    load_test_parser = subparsers.add_parser("loadtest", help="Run a load test on an API endpoint")
    load_test_parser.add_argument("url", help="API URL to load test")
    load_test_parser.add_argument("--requests", type=int, default=10, help="Number of requests to send")

    args = parser.parse_args()

    if args.command == "monitor":
        monitor_api(args.url, args.interval, args.count)
    elif args.command == "loadtest":
        load_test_api(args.url, args.requests)

if __name__ == "__main__":
    main()
