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

**Web Application Security Scanner** is a powerful CLI-based tool for web application vulnerability assessment, designed with flexibility, extensibility, and performance optimization in mind. It supports a comprehensive suite of security tests, ranging from SQL Injection to SSL/TLS analysis, allowing security professionals to detect and mitigate vulnerabilities in web applications.

## **Features**

- **Comprehensive Vulnerability Scanning**: Detects SQL Injection, XSS, CSRF, Command Injection, File Inclusion, and more.
- **Crawling Enhancements**: Advanced web crawling, robots.txt parsing, and XML sitemap discovery.
- **Performance and Concurrency**: Multithreaded scanning for improved speed and efficiency.
- **Proxy and Authentication**: Supports proxy and basic HTTP authentication for complex environments.
- **Advanced Reporting**: Outputs findings in JSON, CSV, and HTML formats for easy analysis and sharing.
- **API Endpoint Scanning**: Targets REST API endpoints.
- **Input Fuzzing**: Identifies potential input validation vulnerabilities.
- **SSL/TLS and Port Scanning**: Evaluates SSL configurations and open ports.
- **DNS Reconnaissance**: Collects DNS records and subdomains for enhanced reconnaissance.

## **Installation**

### Prerequisites

- **Python 3.7+**
- **Pip** package manager

### Step-by-Step Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SushilkumarDev/Web-Application-Security-Scanner.git
   cd Web-Application-Security-Scanner
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**:
   Copy `config.json.example` to `config.json` and adjust settings as necessary.

4. **Run a Test Scan**:

   ```bash
   python cli.py --url http://example.com --scan all
   ```

---

## **Configuration**

Customize your scan settings in `config.json`:

- **scan_threads**: Number of threads for concurrent scanning.
- **proxy**: Proxy settings for routing requests through a proxy server.
- **auth**: Basic authentication credentials (username and password).
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

The CLI scanner is operated through `cli.py`. Use the `--help` flag to see all commands:

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
  - **crawler.py**: Crawls the website and handles robots.txt and sitemap parsing.
  - **vulnerabilities/**: Modules for each type of vulnerability.
    - `sql_injection.py`, `xss.py`, `csrf.py`, etc.: Tests for specific vulnerabilities.
  - **concurrency.py**: Manages threading and performance.
  - **proxy.py**: Configures proxy settings.
  - **fuzzing.py**: Runs fuzzing tests on input fields.
  - **ssl_scanner.py**: Analyzes SSL/TLS configurations.
  - **dns_recon.py**: Performs DNS reconnaissance to detect subdomains and records.

---

## **Detailed Features**

### 1. **Vulnerability Scanners**

**SQL Injection (`sql_injection.py`)**  
Detects SQL injection vulnerabilities by injecting typical SQL payloads into input fields.

**Cross-Site Scripting (XSS) (`xss.py`)**  
Identifies XSS vulnerabilities by injecting scripts and checking execution in the web application's context.

**Cross-Site Request Forgery (CSRF) (`csrf.py`)**  
Looks for missing anti-CSRF tokens, which can expose applications to unauthorized actions.

**Command Injection (`command_injection.py`)**  
Attempts to inject system commands to gain unauthorized access.

---

### 2. **Crawler Enhancements**

- **robots.txt Parsing**: Parses robots.txt for allowable/disallowable paths.
- **Sitemap Crawling**: Extracts URLs from sitemap.xml files.

---

### 3. **Performance and Concurrency**

**Multithreading**  
Configured through `concurrency.py`, allowing concurrent scanning across multiple URLs for improved performance.

---

### 4. **Proxy and Authentication**

**Proxy Support (`proxy.py`)**  
Routes requests through a specified proxy server for controlled testing.

**Authentication (`utils.py`)**  
Supports basic HTTP authentication for accessing secure pages.

---

### 5. **Input Fuzzing (`fuzzing.py`)**

Uses payloads to identify input validation issues, potentially exposing vulnerabilities like SQL Injection and XSS.

---

### 6. **SSL/TLS and Port Scanning**

**SSL Scanner (`ssl_scanner.py`)**  
Evaluates the security of SSL/TLS certificates for validity and proper configuration.

**Port Scanner (`port_scanner.py`)**  
Performs port scanning to identify open ports that may pose threats.

---

### 7. **DNS Reconnaissance**

**DNS Scanner (`dns_recon.py`)**  
Resolves IP addresses, extracts subdomains, and identifies misconfigured DNS records.

---

## **Advanced Customization**

To add or modify scan modules:

1. **Create a new file** in the `vulnerabilities/` directory.
2. Implement the vulnerability check using the `requests` library or another suitable tool.
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

- **JSON**: Stores scan results in a structured format for integration with other tools.
- **CSV**: Provides a tabular format for spreadsheet use.
- **HTML**: Offers a visual representation of scan results with categorized vulnerabilities.

**Example: Generating an HTML Report**

```bash
python cli.py --url http://example.com --scan all --report html
```

Output will be saved to `scan_report.html` in the project root.

---

## **Contributing**

We welcome contributions! Please follow these guidelines:

1. **Fork the Repository**: Create your fork on GitHub.
2. **Branch for Feature**: Create a new branch (`feature/new-scan`).
3. **Write Tests**: Ensure new functionality is tested.
4. **Pull Request**: Submit a pull request, ensuring your code passes all checks.

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## **License**

This project is licensed under the GNU General Public License v3.0 License. See [LICENSE](LICENSE) for more information.

---

This documentation provides users with essential information for operating, customizing, and extending the Web Application Security Scanner. Each link will open the respective file for further details.
