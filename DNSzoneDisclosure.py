import dns.query
import dns.zone
import dns.resolver

def check_zone_transfer(domain, dns_server):
    try:
        # Attempting the DNS zone transfer
        zone = dns.zone.from_xfr(dns.query.xfr(dns_server, domain))

        if zone is not None:
            print(f"[+] Zone transfer successful for {domain} using DNS server {dns_server}.")
            for name, node in zone.nodes.items():
                print(name.to_text(), node.to_text(zone.origin))
        else:
            print(f"[-] Zone transfer failed or no records returned for {domain}.")
    except Exception as e:
        print(f"[-] An error occurred: {str(e)}")

if __name__ == "__main__":
    domain = input("Enter the domain name to check: ")
    dns_server = input("Enter the DNS server IP: ")
    
    check_zone_transfer(domain, dns_server)
