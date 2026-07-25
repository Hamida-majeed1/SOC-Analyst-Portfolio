# Real Attack Mapping Lab

## Attack Scenario

An employee receives a phishing email with a malicious attachment.
The employee opens the attachment, which executes malware.
The malware installs itself, steals user credentials, and sends confidential files to the attacker's server.

---

## Cyber Kill Chain Mapping

| Stage | Activity |
|--------|----------|
| Reconnaissance | Attacker collected employee email addresses |
| Weaponization | Malware embedded in Word document |
| Delivery | Phishing email sent |
| Exploitation | User opened the attachment |
| Installation | Malware installed |
| Command and Control | Malware connected to attacker server |
| Actions on Objectives | Company data stolen |

---

## MITRE ATT&CK Mapping

| Tactic | Technique | ID |
|---------|-----------|----|
| Initial Access | Phishing | T1566 |
| Execution | PowerShell | T1059.001 |
| Persistence | Registry Run Keys | T1547 |
| Credential Access | OS Credential Dumping | T1003 |
| Exfiltration | Exfiltration Over C2 Channel | T1041 |

---

## Conclusion

This lab demonstrates how a phishing attack can be analyzed using both the Cyber Kill Chain and the MITRE ATT&CK Framework. These frameworks help SOC Analysts understand attacker behavior and improve detection and response.
