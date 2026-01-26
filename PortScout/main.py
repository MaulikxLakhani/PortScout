import argparse
import csv
import socket
import threading

from tabulate import tabulate


class PortScout:
    common_ports = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 88, 110, 111, 119, 123, 135, 137, 138, 139, 143, 161, 179, 389, 
    427, 443, 445, 465, 514, 515, 548, 554, 587, 631, 636, 646, 873, 990, 993, 995, 1025, 1026, 1027, 1028, 1029, 1080, 1433, 
    1521, 1720, 1723, 1755, 1883, 1900, 2000, 2049, 2082, 2083, 2095, 2096, 2375, 2376, 2379, 2380, 3000, 3001, 3002, 3128, 
    3306, 3389, 4000, 4100, 4200, 4201, 4300, 4899, 5000, 5050, 5060, 5357, 5432, 5601, 5666, 5672, 5800, 5900, 5901, 5902, 
    5903, 5984, 6000, 6001, 6081, 6082, 6379, 6443, 7070, 8000, 8008, 8009, 8080, 8081, 8082, 8085, 8086, 8100, 8200, 8443, 
    8883, 8888, 8983, 9000, 9001, 9042, 9090, 9092, 9100, 9200, 9229, 9300, 9443, 9999, 10000, 11211, 27017, 27018, 32768, 50070, 50075]

    port_services = {
        20: "ftp-data",
        21: "ftp",
        22: "ssh",
        23: "telnet",
        25: "smtp",
        53: "domain",
        67: "bootps",
        68: "bootpc",
        69: "tftp",
        80: "http",
        88: "kerberos",
        110: "pop3",
        111: "rpcbind",
        119: "nntp",
        123: "ntp",
        135: "msrpc",
        137: "netbios-ns",
        138: "netbios-dgm",
        139: "netbios-ssn",
        143: "imap",
        161: "snmp",
        179: "bgp",
        389: "ldap",
        427: "svrloc",
        443: "https",
        445: "microsoft-ds",
        465: "smtps",
        514: "shell",
        515: "lpd",
        548: "afp",
        554: "rtsp",
        587: "submission",
        631: "ipp",
        636: "ldaps",
        646: "ldp",
        873: "rsync",
        990: "ftps",
        993: "imaps",
        995: "pop3s",
        1025: "unknown",
        1026: "unknown",
        1027: "unknown",
        1028: "unknown",
        1029: "unknown",
        1080: "socks",
        1433: "mssql",
        1521: "oracle",
        1720: "h323",
        1723: "pptp",
        1755: "wms",
        1883: "mqtt",
        1900: "ssdp",
        2000: "cisco-sccp",
        2049: "nfs",
        2082: "cpanel",
        2083: "cpanel-ssl",
        2095: "webmail",
        2096: "webmail-ssl",
        2375: "docker",
        2376: "docker-ssl",
        2379: "etcd",
        2380: "etcd-server",
        3000: "node",
        3001: "unknown",
        3002: "unknown",
        3128: "squid",
        3306: "mysql",
        3389: "rdp",
        4000: "unknown",
        4100: "unknown",
        4200: "unknown",
        4201: "unknown",
        4300: "unknown",
        4899: "radmin",
        5000: "unknown",
        5050: "unknown",
        5060: "sip",
        5357: "wsd",
        5432: "postgresql",
        5601: "kibana",
        5666: "nrpe",
        5672: "amqp",
        5800: "vnc-http",
        5900: "vnc",
        5901: "vnc",
        5902: "vnc",
        5903: "vnc",
        5984: "couchdb",
        6000: "x11",
        6001: "x11",
        6081: "varnish",
        6082: "varnish-admin",
        6379: "redis",
        6443: "kubernetes",
        7070: "realserver",
        8000: "http-alt",
        8008: "http-alt",
        8009: "ajp13",
        8080: "http-proxy",
        8081: "http-alt",
        8082: "http-alt",
        8085: "http-alt",
        8086: "influxdb",
        8100: "unknown",
        8200: "vault",
        8443: "https-alt",
        8883: "mqtts",
        8888: "http-alt",
        8983: "solr",
        9000: "sonarqube",
        9001: "tor-orport",
        9042: "cassandra",
        9090: "unknown",
        9092: "kafka",
        9100: "jetdirect",
        9200: "elasticsearch",
        9229: "node-debug",
        9300: "elasticsearch-transport",
        9443: "https-alt",
        9999: "unknown",
        10000: "webmin",
        11211: "memcached",
        27017: "mongodb",
        27018: "mongodb",
        32768: "unknown",
        50070: "hadoop-namenode",
        50075: "hadoop-datanode",
    }

    def __init__(self):
        self.results = []

    def scan_port(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                if sock.connect_ex((ip, port)) == 0:
                    service_name = socket.getservbyport(port, 'tcp')
                    banner = "Banner not found"
                    if port in [80, 443]:
                        try:
                            sock.sendall(f'GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n'.encode())
                            response = sock.recv(1024).decode(errors='ignore').split('\r\n')
                            banner = next(
                                (header.split(': ', 1)[1].strip() for header in response if
                                 header.startswith("Server:")),
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
        group.add_argument('-d', nargs='+', help="List of up to 200 domains/IP addresses", metavar="Domain or IP")
        group.add_argument('-t', help="File containing list of domains/IP addresses", metavar="File containing targets")
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
            print("Results exported as results.csv in the current directory.")


if __name__ == "__main__":
    PortScout().main()
