
Example:

# Real Attack: Phishing Attack

## 1. Attack Scenario

An attacker sends a phishing email to a victim containing a malicious link. The victim clicks the link, downloads malware, and the attacker gains access to the system.

---

# Cyber Kill Chain Mapping

| Kill Chain Stage      | Attacker Activity                     |
| --------------------- | ------------------------------------- |
| Reconnaissance        | Collect victim email information      |
| Weaponization         | Create malicious link/file            |
| Delivery              | Send phishing email                   |
| Exploitation          | Victim opens malicious link           |
| Installation          | Malware installed on system           |
| Command & Control     | Attacker controls compromised machine |
| Actions on Objectives | Steal data                            |

---

# MITRE ATT&CK Mapping

| Activity             | Tactic            | Technique                    | ID        |
| -------------------- | ----------------- | ---------------------------- | --------- |
| Phishing email       | Initial Access    | Phishing                     | T1566     |
| Run malicious script | Execution         | PowerShell                   | T1059.001 |
| Steal passwords      | Credential Access | OS Credential Dumping        | T1003     |
| Send stolen data     | Exfiltration      | Exfiltration Over C2 Channel | T1041     |

---

# Detection (Blue Team)

* Email security monitoring
* SIEM alerts
* PowerShell logging
* Endpoint detection
* User awareness training
