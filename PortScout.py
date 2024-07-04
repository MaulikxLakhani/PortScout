import argparse
import csv
import socket
import threading

from tabulate import tabulate

common_ports = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 179, 389, 443, 445,
                465, 514, 636, 993, 995, 1080, 1433, 1521, 2049, 3306, 3389, 5432, 5800, 5900, 5984, 6379, 8080, 8443,
                9090, 27017, 27018, 50070, 50075, 8020, 8088]


def scan_port(ip, port, results):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if not sock.connect((ip, port)):
                service_name = socket.getservbyport(port, 'tcp')
                if port in [80, 443]:
                    try:
                        sock.sendall(b'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % ip.encode())
                        response = sock.recv(1024).decode(errors='ignore').split('\r\n')
                        banner = next(
                            (header.split(': ', 1)[1].strip() for header in response if header.startswith("Server:")),
                            "Banner not available")
                    except Exception as e:
                        print(f"Error: {e}")
                        banner = "Banner could not be retrieved."
                else:
                    banner = sock.recv(1024).decode(errors='ignore').strip()
                results.append((ip, port, "Open", service_name, banner))
            else:
                results.append((ip, port, "Closed", "", ""))
    except socket.error:
        results.append((ip, port, "Error", "", ""))


def start_scanning(ip, results):
    threads = [threading.Thread(target=scan_port, args=(ip, port, results)) for port in common_ports]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def parse_args():
    parser = argparse.ArgumentParser(description="Port Scanner and Banner Grabber")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', nargs='+', help="List of up to 100 domains/IP addresses", metavar="IP")
    group.add_argument('-l', help="File containing list of domains/IP addresses", metavar="FILE")
    return parser.parse_args()


def read_ips_from_file(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file if line.strip()]


def validate_targets(targets):
    return [socket.gethostbyname(target) for target in targets if socket.gethostbyname(target)]


if __name__ == "__main__":
    args = parse_args()
    targets = args.d if args.d else read_ips_from_file(args.l)
    if not targets or len(targets) > 200:
        exit(print("You can supply up to 200 domains/IP addresses."))

    valid_targets = validate_targets(targets)
    if not valid_targets:
        exit(print("No valid domains/IP addresses to scan."))

    results = []
    for target in valid_targets:
        start_scanning(target, results)

    open_ports = [result for result in results if result[2] == "Open"]
    print(tabulate(open_ports, headers=["IP Address", "Port", "Status", "Service", "Banner"], tablefmt="pretty"))
    # Write results to result.csv
    with open('PortScan.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Port", "Status", "Service", "Banner"])
        writer.writerows(open_ports)
