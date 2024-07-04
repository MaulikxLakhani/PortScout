# PortScout - High Performance Port Scanner

## 📜 Description

PortScout is a fast and efficient network port scanner for common ports. This script performs rapidly fast scanning of supplied IP addresses and domain names to check common ports. While conducting a targeted security audit, PortScout provides the critical information you need to keep your systems secure.

## 🌟 Features

- **Port Check**: Identifies open ports and provides service name.
- **Banner Retrieval**: Efficiently retrieves SSH, HTTP banners without authentication.
- **Multi-threading**: Uses threading for concurrent checks, significantly reducing scan times.
- **Detailed Output**: Provides clear output summarizing scan result.

## 🚀 Usage

```bash
python PortScout.py <targets>
```

### Examples

#### Single domain or IP

```bash
python PortScout.py -d 192.168.1.1
```

#### Multiple domains and IPs

```bash
python PortScout.py -d 91.191.200.30 proxy.domain.com
```

#### List of targets via a text file

```bash
python PortScout.py -l targets.txt
```

## Output

The script will provide a summary of the scanned targets:
```
+--------------+------+--------+---------+-----------------------+
|  IP Address  | Port | Status | Service |        Banner         |
+--------------+------+--------+---------+-----------------------+
| 50.116.1.184 |  80  |  Open  |  http   | Apache/2.4.6 (CentOS) |
| 50.116.1.184 | 443  |  Open  |  https  | Apache/2.4.6 (CentOS) |
| 50.116.1.184 |  22  |  Open  |   ssh   |  SSH-2.0-OpenSSH_7.4  |
+--------------+------+--------+---------+-----------------------+
```
