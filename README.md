# Reverse Shell Detector

This project is a  Python-based tool designed to detect suspicious outbound connections that may indicate a reverse shell attack. It continuously monitors network activity on a Windows machine, identifying established connections that could signal unauthorized remote access.

## Description

This tool provides visibility into live TCP connections, particularly those where a local host unexpectedly initiates outbound connections. It's useful for detecting basic reverse shell activity in lab environments, red team vs. blue team simulations, or cybersecurity awareness exercises.

## How It Works

- Uses `psutil` to inspect active IPv4/IPv6 connections
- Flags any ESTABLISHED connections with remote endpoints
- Prints potential reverse shell indicators every few seconds

## Screenshots

### Reverse Shell Session (Ubuntu to Windows)
![Reverse Shell Active](screenshots/shell-connection.png)

### Detector Catching the Connection
![Detection Output](screenshots/detection-output.png)

## Skills Demonstrated

- Network monitoring and socket inspection
- Real-time system analysis with Python
- Process and connection enumeration using `psutil`
- Adversarial simulation via reverse shell testing
- Defensive script design for host-based detection

## How This Is Useful in a Work Environment

Reverse shells are commonly used by attackers to gain remote access to compromised systems. This project demonstrates the ability to detect such behavior at the host level by monitoring active outbound connections in real time. In a professional environment, tools like this can help security teams identify unauthorized activity, support incident response, and reduce dwell time.

This project reflects practical knowledge of threat detection, network behavior analysis, and defensive programming—skills applicable in roles such as SOC analyst, blue team operator, or cybersecurity engineer.

## Requirements

- Python 3.x
- `psutil` library

Install with:

```bash
pip install psutil
