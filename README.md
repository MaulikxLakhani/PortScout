# PortScout - High Performance Port Scanner

## 📜 Description

PortScout is a fast and efficient network port scanner for common ports. This script performs rapid-fast scanning of supplied IP addresses and domain names to check common ports. While conducting a targeted security audit, PortScout provides the critical information you need to secure your systems. Ideally, it takes 2 minutes to scan 100 domains/IPs.

## 📜 Why PortScout?

- **Built from scratch**: Highly efficient with tiny codebase. NO NEED of: venv, random dependencies, dependency version conflicts.
- **"Speed. I am speed"**: Just like Lightning McQueen, this tool is superfast and solid. 
- **Auto validation**: Quickly checks your supplied domain, subdomain, IP is valid/alive or not.
- **Service Banner by default**: Gives you service banner - name and version by default that too at superfast speed. No additional flag or switch needed.
- **Built Different**: Establieshes a socket connection to specified ports.
- **Usable Output**: Gives you an output in table format on CLI, by default outputs a results.csv. Easy to integrate in any workflow.

## 🌟 Features

- **Multi-threading**: Uses threading for concurrent checks, significantly reducing scan times.
- **Port Check**: Identifies open ports and provides service name.
- **Banner Retrieval**: Efficiently retrieves SSH, and HTTP banners without authentication.
- **Detailed Output**: Provides clear output summarizing scan results.

## 🚀 Install

```bash
pip install PortScout
```

## 🚀 Usage

```bash
PortScout -d <target1, target2>
PortScout -t <targets.txt>
```

### Examples

#### Single domain or IP

```bash
PortScout -d 192.168.1.1
```

#### Multiple domains and IPs

```bash
PortScout -d 91.191.200.30 proxy.domain.com
```

#### List of targets via a text file

```bash
PortScout -t targets.txt
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
Results will be exported as results.csv in the current directory.

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

Feature Request
-------------
To request a new feature, create a "new issue" and describe the feature and potential use cases. You can upvote the "issue" and contribute to the discussions if something similar already exists.

Authors
-------------
Project Founder
*   Maulik Lakhani - [LinkedIn](https://in.linkedin.com/in/mauliklakhani)

Contributors
*   If you want to contribute, please reach out to me on [Twitter](https://twitter.com/MaulikxLakhani) or [LinkedIn](https://in.linkedin.com/in/mauliklakhani) 

How to help
-------------
You can help this project in many ways:
*   Spread this project within your network.
*   Providing your time and coding skills to add more features and stability to the project.
*   Provide access to feeds that detect CVE based on the identified version.
*   Open new issues with new suggestions, ideas, bug reports or feature requests.
*   Share your story about how have you been using the PhishDetect and what impact it brought.

