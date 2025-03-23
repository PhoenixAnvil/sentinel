# Sentinel
A lightweight command-line API Monitoring and Load Testing Tool written in Python.

## Overview
Sentinel is designed to help developers, testers, and quality engineers monitor the health and performance of APIs directly from the command line. This tool provides essential capabilities for monitoring API availability and conducting basic load tests.

## Key Features
- Monitor the availability and health of APIs
- Perform simple load testing with multiple requests
- Lightweight and minimal dependencies
- Easy to use and extend

## Installation
1.	Clone the repository
2.	Navigate to the project directory
3.	Create and activate a virtual environment
4.	Install the required dependencies from requirements.txt

Example:
```
git clone https://github.com/yourusername/sentinel.git
cd sentinel
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Sentinel is a command-line tool with two primary commands:
1.	Monitor a single API endpoint  
Example:  
```
sentinel monitor https://example.com/api/health
```
2.	Load test an API endpoint  
Example:  
```
sentinel loadtest https://example.com/api/health –requests 100
```

## Roadmap
- Add JSON output support
- Add scheduled interval monitoring (periodic checks)
- Add advanced load testing configurations (concurrency, ramp-up)
- Improve reporting with success/failure metrics

## Contributing
This is a personal learning project as part of my professional development. I’m using it to sharpen my skills in Python, testing, and API development. Feedback is welcome, but contributions are not currently being accepted.

## Author
Jason Alan Smith  
- [E-mail](mailto:jason.alan.smith@outlook.com)
- [LinkedIn](https://www.linkedin.com/in/jason-alan-smith)
- [GitHub](https://github.com/PhoenixAnvil)

## License
MIT License