import dns.resolver

def check_dns(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f'IP: {ipval.to_text()}')
    except Exception as e:
        print(f"Error resolving DNS for {domain}: {e}")
