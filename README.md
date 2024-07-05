![image](https://github.com/MaulikxLakhani/PortScout/assets/61105552/99dc4dbe-d300-40de-9eed-4df8ffa9c6a6)# PortScout - High Performance Port Scanner

## 📜 Description

PortScout is a fast and efficient network port scanner for common ports. This script performs rapid-fast scanning of supplied IP addresses and domain names to check common ports. While conducting a targeted security audit, PortScout provides the critical information you need to keep your systems secure. Ideally, it takes 2 minutes to scan 100 domains/IPs.

## 🌟 Features

- **Multi-threading**: Uses threading for concurrent checks, significantly reducing scan times.
- **Port Check**: Identifies open ports and provides service name.
- **Banner Retrieval**: Efficiently retrieves SSH, HTTP banners without authentication.
- - **Detailed Output**: Provides clear output summarizing scan result.

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
python PortScout.py -t targets.txt
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

## Speed Comparison

PortScout vs Nmap speed comparison:
```
+-----------+------------------+-----------------+---------+----------------+
| Tool Name | Total Domains/IP | Live Domains/IP | Command |   Time Taken   |
+-----------+------------------+-----------------+---------+----------------+
| PortScout |        30        |       25        |         |   30 seconds   |
|   Nmap    |        30        |       25        | -T4 -F  | 223.40 seconds |
+-----------+------------------+-----------------+---------+----------------+
```
