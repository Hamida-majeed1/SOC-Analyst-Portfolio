# Windows Hardening Guide

## Objective

The purpose of Windows hardening is to reduce the attack surface, protect user accounts, disable unnecessary remote access, and verify important security controls.

## 1. Check Local User Accounts

**Command:**

```powershell
Get-LocalUser
```

**Purpose:**
To identify local user accounts and check whether built-in accounts are enabled or disabled.

**Finding:**
The built-in **Administrator, Guest, and DefaultAccount** accounts were disabled. The primary user account was enabled.

---

## 2. Check Administrators Group

**Command:**

```powershell
Get-LocalGroupMember Administrators
```

**Purpose:**
To identify which accounts have administrative privileges.

**Finding:**
The built-in Administrator account and the primary user account were members of the Administrators group. The Administrator account itself was disabled.

---

## 3. Check Remote Desktop

**Command:**

```powershell
Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections
```

**Purpose:**
To determine whether Remote Desktop Protocol (RDP) connections are enabled.

**Finding:**

```text
fDenyTSConnections : 1
```

`1` means RDP is **disabled**, reducing the risk of unauthorized remote access.

---

## 4. Review Running Services

**Command:**

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
```

**Purpose:**
To review currently running Windows services and identify unnecessary or suspicious services.

**SOC Relevance:**
Attackers may create or abuse services for **persistence, privilege escalation, or execution**.

---

## 5. Check Microsoft Defender

**Command:**

```powershell
Get-MpComputerStatus
```

**Purpose:**
To verify the health and protection status of Microsoft Defender.

**Finding:**

* Antivirus: **Enabled**
* Antispyware: **Enabled**
* Real-time protection: **Enabled**
* Behavior monitoring: **Enabled**
* Security signatures: **Up to date**
* Tamper protection: **Enabled**

---

## 6. Check Windows Firewall

**Command:**

```powershell
Get-NetFirewallProfile
```

**Purpose:**
To verify the status of Windows Firewall profiles.

**Finding:**
Domain, Private, and Public firewall profiles were **enabled**.

---

## 7. Review Firewall Rules

**Command:**

```powershell
Get-NetFirewallRule
```

**Purpose:**
To review configured inbound and outbound firewall rules.

**SOC Relevance:**
Firewall rules can help identify unnecessary or suspicious network access. An analyst should review the **rule name, direction, action, enabled status, application, port, and profile**.

---

## Security Conclusion

The Windows system was reviewed for common hardening areas including **user accounts, administrative privileges, RDP, running services, Microsoft Defender, and Windows Firewall**. These checks help reduce the attack surface and support Blue Team/SOC monitoring.
