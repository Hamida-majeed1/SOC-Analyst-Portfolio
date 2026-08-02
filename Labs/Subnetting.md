# Day 10 - Subnetting Lab

## Lab 1

**IP Address:** 192.168.1.75/26

- Block Size: 64
- Network Address: 192.168.1.64
- Broadcast Address: 192.168.1.127
- First Host: 192.168.1.65
- Last Host: 192.168.1.126
- Usable Hosts: 62

---

## Lab 2

**IP Address:** 10.0.0.78/26

- Block Size: 64
- Network Address: 10.0.0.64
- Broadcast Address: 10.0.0.127
- First Host: 10.0.0.65
- Last Host: 10.0.0.126
- Usable Hosts: 62

---

## Lab 3

**IP Address:** 192.168.100.141/27

- Block Size: 32
- Network Address: 192.168.100.128
- Broadcast Address: 192.168.100.159
- First Host: 192.168.100.129
- Last Host: 192.168.100.158
- Usable Hosts: 30

---

## Lab 4

**IP Address:** 172.16.5.222/28

- Block Size: 16
- Network Address: 172.16.5.208
- Broadcast Address: 172.16.5.223
- First Host: 172.16.5.209
- Last Host: 172.16.5.222
- Usable Hosts: 14

---

## Lab 5

**IP Address:** 192.168.50.130/25

- Block Size: 128
- Network Address: 192.168.50.128
- Broadcast Address: 192.168.50.255
- First Host: 192.168.50.129
- Last Host: 192.168.50.254
- Usable Hosts: 126

---

## SOC Analyst Scenario

**Scenario:**

A firewall log shows repeated malicious traffic from:

**Source IP:** `192.168.100.141/27`

**Task:** Identify the subnet to block.

**Answer:**

- Subnet to Block: `192.168.100.128/27`

**Reason:**

Blocking the subnet `192.168.100.128/27` prevents all hosts within that subnet from communicating through the firewall, helping contain the malicious activity.
