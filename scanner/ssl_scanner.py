import ssl
import socket

def check_ssl(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            print(f"SSL Certificate for {hostname}:")
            print(cert)
            # Check for expired certificates or weak encryption here
