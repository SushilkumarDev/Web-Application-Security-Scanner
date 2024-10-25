import socket

def scan_ports(hostname, port_range=(1, 1024)):
    open_ports = []
    for port in range(*port_range):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((hostname, port))
            if result == 0:
                print(f"Port {port} is open on {hostname}")
                open_ports.append(port)
    return open_ports
