import argparse

from sentinel.load_test import load_test_api
from sentinel.monitor import monitor_api


def parse_count(value):
    """Allow --count None to be passed as a string from the CLI."""
    return None if value.lower() == "none" else int(value)


def main():
    parser = argparse.ArgumentParser(
        prog="Sentinel",
        description="API Monitoring & Load Testing CLI Tool",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Monitor command
    monitor_parser = subparsers.add_parser(
        "monitor", help="Monitor an API endpoint"
    )
    monitor_parser.add_argument("url", help="API URL to monitor")
    monitor_parser.add_argument(
        "--interval",
        type=int,
        default=0,
        help="Monitoring interval (in seconds)",
    )
    monitor_parser.add_argument(
        "--count",
        type=parse_count,
        default=None,
        help='Number of times to poll. Use "None" to poll indefinitely.',
    )

    # Load Test command
    load_test_parser = subparsers.add_parser(
        "loadtest", help="Run a load test on an API endpoint"
    )
    load_test_parser.add_argument("url", help="API URL to load test")
    load_test_parser.add_argument(
        "--requests",
        type=int,
        default=10,
        help="Number of requests to send",
    )

    args = parser.parse_args()

    if args.command == "monitor":
        monitor_api(args.url, args.interval, args.count)
    elif args.command == "loadtest":
        load_test_api(args.url, args.requests)


if __name__ == "__main__":
    main()
