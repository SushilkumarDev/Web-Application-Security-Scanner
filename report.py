import json
import csv

def generate_json_report(vulnerabilities):
    with open("scan_report.json", "w") as json_file:
        json.dump(vulnerabilities, json_file, indent=4)
    print("JSON report generated: scan_report.json")

def generate_csv_report(vulnerabilities):
    with open("scan_report.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Vulnerability", "URL", "Details"])
        for vuln in vulnerabilities:
            writer.writerow([vuln['type'], vuln['url'], vuln['details']])
    print("CSV report generated: scan_report.csv")

def generate_html_report(vulnerabilities):
    with open("scan_report.html", "w") as html_file:
        html_file.write("<html><head><title>Scan Report</title></head><body>")
        html_file.write("<h1>Web Application Security Scan Report</h1>")
        for vuln in vulnerabilities:
            html_file.write(f"<h2>Vulnerability: {vuln['type']}</h2>")
            html_file.write(f"<p>URL: {vuln['url']}</p>")
            html_file.write(f"<p>Details: {vuln['details']}</p>")
        html_file.write("</body></html>")
    print("HTML report generated: scan_report.html")
