<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=000000,300000,ff0000&height=240&section=header&text=NeuralMind&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Modular%20Security%20Intelligence%20Core&descAlignY=60&descSize=20" width="100%"/>

  <p>
    <img src="https://img.shields.io/badge/Version-1.0.0-cb2d3e?style=for-the-badge&labelColor=000000" />
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Architecture-Modular-orange?style=for-the-badge&logo=hive&logoColor=white" />
    <img src="https://img.shields.io/badge/Focus-Red_Team-red?style=for-the-badge&logo=kalilinux&logoColor=white" />
  </p>

</div>

---

### 🧠 System Overview
**NeuralMind** is an extensible, modular security framework designed to centralize Red Team operations. Unlike monolithic scripts, NeuralMind utilizes a "Core" architecture that dynamically loads specialized modules for reconnaissance, static analysis, and covert operations.

This framework is built for **scalability**—new offensive or defensive capabilities can be integrated simply by dropping a Python script into the `/modules` directory, automatically registering it with the central CLI.

---

### 📦 Core Arsenal

| Module | Codename | Classification | Status |
| :--- | :--- | :--- | :--- |
| **Static Analysis** | `Cortex` | **SAST** | ✅ Active |
| **Steganography** | `Ghost` | **Cryptography** | ✅ Active |
| **Network Recon** | `Vision` | **Intelligence** | ✅ Active |

---

### ⚙️ Deployment & Installation

Follow these steps to deploy NeuralMind in your local environment.

#### 1. Clone the Repository
```bash
git clone [https://github.com/devnand-47/NeuralMind.git](https://github.com/devnand-47/NeuralMind.git)
cd NeuralMind
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Initialize the Core
Bash

python main.py
📘 Operations Manual
1. Cortex (Vulnerability Scanner)
Function: Performs Static Application Security Testing (SAST) on source code to identify insecure coding patterns.

Vectors Scanned: Hardcoded credentials, exec()/eval() usage, SQL injection vulnerabilities.

Usage:

Plaintext

[NeuralMind] > Select Module: 1
[Cortex] > Enter target file: targets/vulnerable_test.py

[!] ALERT: Hardcoded Password detected.
[!] ALERT: SQL Injection Risk detected.
2. Ghost (Steganography)
Function: Implements Least Significant Bit (LSB) steganography to hide encrypted text payload inside image files for covert communication.

Modes: (E)ncrypt (Hide data) / (D)ecrypt (Reveal data).

Constraints: Supports .png files to prevent data loss via compression.

Usage:

Plaintext

[NeuralMind] > Select Module: 2
[Ghost] > Mode: E
[Ghost] > Target Image: targets/cover.png
[Ghost] > Payload: "Operation starting at midnight."
[+] Success. Output saved to secret_image.png
3. Vision (Network Reconnaissance)
Function: Maps local subnets to identify active hosts and open service ports.

Method: Raw socket connections and ICMP requests.

Demo Limit: Scans IPs 1-50 in the detected subnet.

Usage:

Plaintext

[NeuralMind] > Select Module: 3
[Vision] > Enter Target IP: 192.168.1.1

[*] Scanning Subnet...
[+] Host Up: 192.168.1.1 (Gateway)
[+] Host Up: 192.168.1.45 (Workstation)
📂 Architecture Structure
Bash

NeuralMind/
├── modules/             # Plug-and-Play Capabilities
│   ├── __init__.py      # Package Initialization
│   ├── cortex.py        # SAST Logic
│   ├── ghost.py         # Stego Logic
│   └── vision.py        # Socket Logic
├── targets/             # Firing Range (Test files)
├── main.py              # Central CLI Controller
└── requirements.txt     # Dependency Manifest
⚠️ Legal Disclaimer
This tool is for educational purposes and internal security testing only.

The developer (Dev_Nand) is not responsible for any misuse or damage caused by this program. NeuralMind is intended to demonstrate modular software architecture in a cybersecurity context. Never scan networks or systems without explicit permission.

<div align="center"> <h3>Developed with 💀 by <a href="https://github.com/devnand-47">Dev_Nand</a></h3> </div>
