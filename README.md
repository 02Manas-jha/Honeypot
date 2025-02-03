# Honeypot Project

This repository contains a Python-based medium-interaction honeypot designed to log connection attempts and basic attacker behavior, as well as a stimulation script to test the honeypot's functionality. The honeypot aims to serve as a security tool to detect and analyze unauthorized access attempts. Additionally, enhancements are planned to improve log analysis by introducing temporal and behavioral pattern identification.

---

## Features

- **Medium Interaction Honeypot**:
  - Captures connection attempts and logs attacker behavior.
  - Mimics limited interaction with attackers to gather data.

- **Logging**:
  - Tracks IP addresses, timestamps, and actions performed by the attacker.
  - Generates logs for further analysis.

- **Testing Stimulation**:
  - `honeypot_sim.py` script to simulate attack scenarios and validate honeypot functionality.

- **Planned Enhancements**:
  - Temporal pattern analysis: Identifying attack trends over time.
  - Behavioral pattern analysis: Detecting recurring attacker behaviors and anomalies.


---

## Getting Started

### Prerequisites

- Python 3.7 or above
- Recommended: Virtual environment to manage dependencies

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/02Manas-jha/Honeypot.git
   cd honeypot-project

2. Usage
    - Running the Honeypot and to test the simulation
    ```bash
    python honypot.py
    python honeypot_sim.py