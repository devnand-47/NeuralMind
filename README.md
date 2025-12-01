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
```
⚠️ Legal Disclaimer
NeuralMind is intended strictly for educational purposes, ethical hacking, internal testing, and research.
The developer (Dev_Nand) is not responsible for misuse, damage, or unauthorized activities.
Never scan systems or networks without explicit permission
```

### 🧠 System Overview

**NeuralMind** is an extensible, modular security framework designed to centralize Red Team operations.  
Unlike monolithic tools, NeuralMind uses a **Core + Modules** architecture where each capability is a plug-and-play Python script placed inside the `/modules` directory.

New offensive or defensive modules can be added instantly — no rewrites needed.

---

### 📦 Core Arsenal

| Module | Codename | Classification | Status |
| :--- | :--- | :--- | :--- |
| **Static Analysis** | `Cortex` | **SAST** | ✅ Active |
| **Steganography** | `Ghost` | **Cryptography** | ✅ Active |
| **Network Recon** | `Vision` | **Intelligence** | ✅ Active |

---

### ⚙️ Deployment & Installation

#### **1. Clone the Repository**
```bash
git clone https://github.com/devnand-47/NeuralMind.git
cd NeuralMind
pip install -r requirements.txt
python main.py
```
📘 Operations Manual

1. Cortex — Static Analysis (SAST)

Identifies insecure coding patterns inside Python source files.

Scans for:

Hardcoded credentials

Dangerous calls (exec, eval)

SQL injection patterns

Weak input sanitization

Usage
```
[NeuralMind] > Select Module: 1
[Cortex] > Enter target file: targets/test.py

[!] ALERT: Hardcoded Password detected.
[!] ALERT: SQL Injection Risk detected.
```
2. Ghost — Steganography (LSB)

Hides encrypted text payloads inside PNG images using Least Significant Bit encoding.

Modes:

E → Embed (Encrypt + Hide)

D → Decode (Reveal hidden data)

Constraints:

Only `.png` supported (lossless)

Usage
```
[NeuralMind] > Select Module: 2
[Ghost] > Mode: E
[Ghost] > Target Image: targets/cover.png
[Ghost] > Payload: "Operation starting at midnight."

[+] Success. Output saved to secret_image.png
```
3. Vision — Network Reconnaissance

Maps local subnet and identifies alive hosts with lightweight active scanning.

Techniques:

ICMP Echo Requests

Raw Socket Connections

Demo Limits:

Scans IPs 1–50 in the detected subnet

Usage
```
[NeuralMind] > Select Module: 3
[Vision] > Enter Target IP: 192.168.1.1

[*] Scanning Subnet...
[+] Host Up: 192.168.1.1 (Gateway)
[+] Host Up: 192.168.1.45 (Workstation)
```
📂 Architecture Structure
```
NeuralMind/
├── modules/             # Plug-and-Play Capabilities
│   ├── __init__.py      # Package Initialization
│   ├── cortex.py        # SAST Logic
│   ├── ghost.py         # Stego Logic
│   └── vision.py        # Socket Logic
├── targets/             # Firing Range (Test files)
├── main.py              # Central CLI Controller
└── requirements.txt     # Dependency Manifest
```
⚠️ Legal Disclaimer

NeuralMind is intended strictly for educational purposes, ethical hacking, internal testing, and research.
The developer (Dev_Nand) is not responsible for misuse, damage, or unauthorized activities.
Never scan systems or networks without explicit permission.

<div align="center"> <h3>Developed  by <a href="https://github.com/devnand-47">Dev_Nand</a></h3> </div> 


