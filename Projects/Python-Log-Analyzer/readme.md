
# Python Log Analyzer

## Overview

A Python-based log analysis tool that analyzes authentication logs, detects failed login attempts, identifies suspicious IP addresses, and generates CSV and JSON reports.

## Objective

The objective of this project is to practice Python file handling and basic SOC-style log analysis.

## Technologies Used

- Python
- CSV
- JSON
- File Handling
- Dictionaries
- Loops
- Conditions
- String Parsing

## Project Structure

```text
Python-Log-Analyzer/
├── log_analyzer.py
├── login.log
├── failed_ips.csv
└── failed_ips.json
````

## Detection Logic

The program uses a threshold of **3 failed login attempts**.

If an IP address reaches or exceeds this threshold, it is identified as suspicious.

## Example Output

```text
User Failed Logins:
Ali 3

IP Failed Logins:
192.168.1.20 3

Suspicious IPs:
192.168.1.20 3
```

## Reports

* `failed_ips.csv` — Stores failed IP addresses and attempt counts.
* `failed_ips.json` — Stores failed IP information in JSON format.

## Skills Practiced

* Python file handling
* Log parsing
* String manipulation
* Dictionary-based counting
* Threshold-based detection
* CSV and JSON report generation
* Basic security log analysis

## What I Learned

This project helped me understand how Python can be used to process authentication logs, count failed login attempts, identify suspicious IP addresses, and generate security reports.

**Read → Parse → Count → Detect → Report → Verify**

```
```
