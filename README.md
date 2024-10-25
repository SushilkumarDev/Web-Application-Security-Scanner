Certainly! Here’s a comprehensive documentation guide for the **Web Application Security Scanner** project, written to the highest standard, covering every detail for ease of use, development, and customization.

---

# **Web Application Security Scanner**

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [CLI Commands](#cli-commands)
7. [Feature Modules and File Structure](#feature-modules-and-file-structure)
8. [Detailed Features](#detailed-features)
9. [Advanced Customization](#advanced-customization)
10. [Reporting](#reporting)
11. [Contributing](#contributing)
12. [License](#license)

---

## **Introduction**

**Web Application Security Scanner** is a powerful, CLI-based security tool for web application vulnerability assessment, designed with flexibility, extensibility, and performance optimization in mind. It supports a comprehensive suite of security tests, ranging from SQL Injection to SSL/TLS analysis, allowing security professionals to detect and mitigate vulnerabilities in web applications.

## **Features**

- **Comprehensive Vulnerability Scanning**: Detects SQL Injection, XSS, CSRF, Command Injection, File Inclusion, and more.
- **Crawling Enhancements**: Includes advanced web crawling, robots.txt parsing, and XML sitemap discovery.
- **Performance and Concurrency**: Supports multithreaded scanning to improve speed and efficiency.
- **Proxy and Authentication**: Integrates proxy and basic HTTP authentication for complex environments.
- **Advanced Reporting**: Outputs findings in JSON, CSV, and HTML formats for easy analysis and sharing.
- **API Endpoint Scanning**: Specifically targets REST API endpoints.
- **Input Fuzzing**: Identifies potential input validation vulnerabilities.
- **SSL/TLS and Port Scanning**: Evaluates SSL configurations and open ports on the target.
- **DNS Reconnaissance**: Collects DNS records and subdomains for enhanced recon.

## **Installation**

### Prerequisites

- **Python 3.7+**
- **Pip** package manager

### Step-by-Step Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/web-sec-scanner.git
   cd web-sec-scanner
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**:
   Copy the `config.json.example` to `config.json` and adjust settings as necessary.

4. **Run a Test Scan**:
   ```bash
   python cli.py --url http://example.com --scan all
   ```

---

## **Configuration**

Customize your scan settings in `config.json`:

- **scan_threads**: Number of threads for concurrent scanning.
- **proxy**: Proxy settings for routing requests through a proxy server.
- **auth**: Set up basic authentication credentials (username and password).
- **timeout**: Request timeout in seconds.

Example `config.json`:

```json
{
  "scan_threads": 5,
  "proxy": "http://localhost:8080",
  "auth": {
    "username": "user",
    "password": "pass"
  },
  "timeout": 10
}
```

---

## **Usage**

### Basic Command

The CLI-based scanner is operated through `cli.py`. Use the `--help` flag to see all commands:

```bash
python cli.py --help
```

### Example Commands

- **Full Scan**: Scans for all vulnerabilities on the target URL.

  ```bash
  python cli.py --url http://example.com --scan all
  ```

- **Specific Vulnerability Scan**: Scans only for SQL Injection.

  ```bash
  python cli.py --url http://example.com --scan sql
  ```

- **Report Generation**: Generate a report in JSON format after a scan.
  ```bash
  python cli.py --url http://example.com --scan all --report json
  ```

---

## **CLI Commands**

| Flag        | Description                                       | Example                         |
| ----------- | ------------------------------------------------- | ------------------------------- |
| `--url`     | Target URL                                        | `--url http://example.com`      |
| `--scan`    | Specify the scan type (e.g., `all`, `sql`, `xss`) | `--scan all`                    |
| `--threads` | Set number of concurrent threads                  | `--threads 10`                  |
| `--report`  | Output report format (`json`, `csv`, `html`)      | `--report json`                 |
| `--proxy`   | Proxy server for routing requests                 | `--proxy http://localhost:8080` |
| `--auth`    | Basic authentication (`username:password`)        | `--auth user:pass`              |
| `--timeout` | Request timeout in seconds                        | `--timeout 5`                   |

---

## **Feature Modules and File Structure**

The project is organized into modules, each responsible for specific tasks, making the code easy to navigate and extend.

- **scanner/**: Core scanning logic and individual vulnerability checks.
  - **crawler.py**: Crawls the website, gathers URLs, and handles robots.txt and sitemap parsing.
  - **vulnerabilities/**: Individual modules for each type of vulnerability.
    - `sql_injection.py`, `xss.py`, `csrf.py`, etc.: Tests for specific vulnerabilities.
  - **concurrency.py**: Manages threading and performance improvements.
  - **proxy.py**: Configures proxy settings.
  - **fuzzing.py**: Runs fuzzing tests on input fields.
  - **ssl_scanner.py**: Analyzes SSL/TLS configurations.
  - **dns_recon.py**: Performs DNS reconnaissance to detect subdomains and records.

---

## **Detailed Features**

### 1. **Vulnerability Scanners**

**SQL Injection (`sql_injection.py`)**  
Detects SQL injection vulnerabilities by injecting typical SQL-based payloads into input fields and observing responses.

**Cross-Site Scripting (XSS) (`xss.py`)**  
Identifies XSS vulnerabilities by injecting scripts and checking if they are executed in the web application's context.

**Cross-Site Request Forgery (CSRF) (`csrf.py`)**  
Looks for missing anti-CSRF tokens, which can leave applications vulnerable to unauthorized actions.

**Command Injection (`command_injection.py`)**  
Attempts to inject system commands to gain unauthorized access to the server.

---

### 2. **Crawler Enhancements**

- **robots.txt Parsing**: Parses robots.txt for allowable/disallowable paths.
- **Sitemap Crawling**: Extracts URLs from sitemap.xml files, ensuring comprehensive coverage.

---

### 3. **Performance and Concurrency**

**Multithreading**  
Configured through `concurrency.py`, multithreading allows for concurrent scanning across multiple URLs, dramatically improving performance.

---

### 4. **Proxy and Authentication**

**Proxy Support (`proxy.py`)**  
Routes requests through a specified proxy server, ideal for testing in controlled environments.

**Authentication (`utils.py`)**  
Supports basic HTTP authentication, required for accessing secure web pages.

---

### 5. **Input Fuzzing (`fuzzing.py`)**

Uses payloads to identify input validation issues, potentially exposing vulnerabilities like SQL Injection, XSS, and Directory Traversal.

---

### 6. **SSL/TLS and Port Scanning**

**SSL Scanner (`ssl_scanner.py`)**  
Evaluates the security of SSL/TLS certificates, ensuring they’re valid, not expired, and correctly configured.

**Port Scanner (`port_scanner.py`)**  
Performs port scanning to identify open ports that may expose the server to threats.

---

### 7. **DNS Reconnaissance**

**DNS Scanner (`dns_recon.py`)**  
Resolves IP addresses, extracts subdomains, and identifies potentially misconfigured DNS records.

---

## **Advanced Customization**

To add or modify scan modules:

1. **Create a new file** in the `vulnerabilities/` directory.
2. Implement the vulnerability check using the `requests` library or another appropriate tool.
3. **Register the module** in `scanner.py` by adding it to the `available_scans` dictionary.

Example:

```python
# vulnerabilities/my_custom_vuln.py
import requests

def check(url):
    print(f"Checking for custom vulnerability on {url}")
    # Custom vulnerability check logic here
```

---

## **Reporting**

Reports can be generated in multiple formats:

- **JSON**: Stores scan results in JSON format for easy integration with other tools.
- **CSV**: Provides a tabular format ideal for spreadsheets.
- **HTML**: Visual representation of scan results with categorized vulnerabilities.

**Example: Generating an HTML Report**

```bash
python cli.py --url http://example.com --scan all --report html
```

Output saved to `scan_report.html` in the project root.

---

## **Contributing**

We welcome contributions to this project. Please follow these guidelines:

1. **Fork the Repository**: Create your fork on GitHub.
2. **Branch for Feature**: Create a new branch (`feature/new-scan`).
3. **Write Tests**: Ensure new functionality has accompanying tests.
4. **Pull Request**: Submit a pull request, and ensure your code passes all checks.

For more details, see `CONTRIBUTING.md`.

---

## **License**

This project is licensed under the MIT License. See `LICENSE.md` for more information.

---

This documentation is designed to provide users with all essential information for operating, customizing, and extending the Web

Application Security Scanner.
