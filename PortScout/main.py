import argparse
import csv
import socket
import threading

from tabulate import tabulate

class PortScout:
    common_ports = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 179, 389, 443, 445,
                    465, 514, 636, 993, 995, 1080, 1433, 1521, 2049, 3306, 3389, 5432, 5800, 5900, 5984, 6379, 8080, 8443,
                    9090, 27017, 27018, 50070, 50075, 8020, 8085, 8088]

    def __init__(self):
        self.results = []

    def scan_port(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                if not sock.connect((ip, port)):
                    service_name = socket.getservbyport(port, 'tcp')
                    banner = "Banner not available"
                    if port in [80, 443]:
                        try:
                            sock.sendall(b'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % ip.encode())
                            response = sock.recv(1024).decode(errors='ignore').split('\r\n')
                            banner = next(
                                (header.split(': ', 1)[1].strip() for header in response if header.startswith("Server:")),
                                banner)
                        except:
                            pass
                    else:
                        banner = sock.recv(1024).decode(errors='ignore').strip() or banner
                    self.results.append((ip, port, "Open", service_name, banner))
        except:
            pass

    def start_scanning(self, ip):
        threads = [threading.Thread(target=self.scan_port, args=(ip, port)) for port in self.common_ports]
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Port Scanner and Banner Grabber")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-d', nargs='+', help="List of up to 200 domains/IP addresses", metavar="IP")
        group.add_argument('-t', help="File containing list of domains/IP addresses", metavar="FILE")
        return parser.parse_args()

    def read_ips_from_file(self, file_path):
        with open(file_path) as file:
            return [line.strip() for line in file if line.strip()]

    def validate_targets(self, targets):
        valid_targets = []
        for target in targets:
            try:
                socket.gethostbyname(target)
                valid_targets.append(target)
            except socket.error:
                pass
        return valid_targets

    def main(self):
        args = self.parse_args()
        targets = args.d if args.d else self.read_ips_from_file(args.t)
        if not targets or len(targets) > 200:
            exit(print("You can supply up to 200 domains/IP addresses."))
        valid_targets = self.validate_targets(targets)
        print("Scanning: ", valid_targets)
        if not valid_targets:
            exit(print("No valid domains/IP addresses to scan."))
        for target in valid_targets:
            self.start_scanning(target)
        open_ports = [result for result in self.results if result[2] == "Open"]
        print(tabulate(open_ports, headers=["Domain/IP", "Port", "Status", "Service", "Banner"], tablefmt="pretty"))
        with open('result.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Domain/IP", "Port", "Status", "Service", "Banner"])
            writer.writerows(open_ports)
            print("Results are exported as results.csv in the current directory.")

if __name__ == "__main__":
    PortScout().main()
