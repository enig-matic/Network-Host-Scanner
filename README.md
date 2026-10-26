# Network-Host-Scanner

# 🔍 Python Host & Port Scanner with Banner Grabbing

A simple Python-based network scanning tool that allows users to scan **one host at a time** and check specified ports. It also provides an optional banner-grabbing feature to check whether a service banner can be retrieved from a selected port.

## 🚀 Features

- **Single Host Scanning:** Scan one target IP address at a time.
- **Port Scanning:** Check specified ports on the target host.
- **Optional Banner Grabbing:** Choose whether to attempt banner grabbing by entering `y` when prompted.
- **Banner Detection:** Display the received banner if one is retrieved, or report that no banner was found.

## 🛠️ Technologies Used

- **Python 3** — for implementing the scanning logic.
- **`socket`** — for establishing TCP connections and communicating with services.
- **`scapy`** — for creating and sending network packets, if used in the script.

## 📋 Requirements

- Python 3 installed on your system.
- Install Scapy if your script uses it:

```bash
pip install scapy
```

## 📥 Installation

Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/Network-Host-Scanner.git
```

Navigate to the project directory:

```bash
cd Network-Host-Scanner
```

## ▶️ Usage

Run the script using Python:

```bash
python3 scanner.py
```

## 🏷️ Optional Banner Grabbing

When the script asks whether you want to check the banner, you may see the following prompt:

```text
Are you check the banner if Available (y,n):
```

- Enter `y` to attempt to retrieve the service banner.
- Enter `n` to skip banner grabbing.

If a banner is received, the script displays it. Otherwise, it reports that no banner was found.

**Note:** A missing banner does not necessarily mean the port is closed. The service may not send a banner, may require a protocol-specific request, or may use encrypted communication such as HTTPS.

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only.

- Scan only systems you own or have explicit permission to test.
- Do not use this script to access or probe unauthorized systems.
- Banner grabbing may return incomplete information or no information, depending on the service.

⭐ If you find this project useful for learning Python networking, consider starring the repository!
