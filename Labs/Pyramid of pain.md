

# Pyramid of Pain Practical Lab

## Objective

Analyze a cyber attack using the Pyramid of Pain and identify which indicators cause the most pain to the attacker.

---

## Attack Scenario

A user receives a phishing email.

The user clicks the malicious attachment.

PowerShell executes malicious commands.

The malware creates a Registry Run Key to maintain persistence.

The attacker steals Windows credentials.

The attacker sends stolen data to a Command and Control (C2) server.

---

## Pyramid of Pain Mapping

| Attack Activity                            | Pyramid Level         | Example                                            | Pain to Attacker |
| ------------------------------------------ | --------------------- | -------------------------------------------------- | ---------------- |
| Malware File                               | Hash Values           | SHA256 Hash                                        | Low              |
| C2 Server                                  | IP Address            | 185.10.10.15                                       | Low              |
| Malicious Website                          | Domain Name           | evil-login.com                                     | Medium           |
| Registry Run Key                           | Network/Host Artifact | HKCU\Software\Microsoft\Windows\CurrentVersion\Run | High             |
| PowerShell                                 | Tool                  | PowerShell                                         | Very High        |
| Phishing + PowerShell + Credential Dumping | TTPs                  | T1566, T1059.001, T1003                            | Highest          |

---

## Analysis

* Blocking only the malware hash is easy for attackers to bypass because they can modify the malware to generate a new hash.
* Blocking an IP address provides only temporary protection since attackers can use a different server.
* Blocking a malicious domain is more effective, but attackers can register a new domain.
* Detecting Registry Run Keys makes persistence more difficult for attackers.
* Detecting malicious use of PowerShell forces attackers to change their tools.
* Detecting attacker behaviors (TTPs) such as phishing, PowerShell execution, and credential dumping causes the most pain because attackers must change their entire attack strategy.

---

## Conclusion

The Pyramid of Pain shows that detecting attacker behavior (TTPs) is much more effective than blocking simple indicators like hashes or IP addresses. SOC analysts should focus on behavior-based detection to make attacks more difficult.

