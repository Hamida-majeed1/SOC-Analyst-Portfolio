
# Day 27 — Windows Administration Lab

## Windows Services

### 1. Check Windows Update Service

```powershell
Get-Service wuauserv
````

**Result:**

* Name: `wuauserv`
* Display Name: `Windows Update`
* Initial Status: `Stopped`

### 2. Start Windows Update Service

```powershell
Start-Service wuauserv
```

**Result:** Service started successfully.

### 3. Verify Service Status

```powershell
Get-Service wuauserv
```

**Result:**

* Status: `Running`

### 4. Stop Windows Update Service

```powershell
Stop-Service wuauserv
```

**Result:** Stop operation returned a service/access error.

### 5. Get Detailed Service Information

```powershell
Get-CimInstance Win32_Service -Filter "Name='wuauserv'"
```

### 6. List Running Services

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
```

---

## Task Scheduler

### 7. List Scheduled Tasks

```powershell
Get-ScheduledTask
```

### 8. Find a Specific Scheduled Task

```powershell
Get-ScheduledTask -TaskName "TaskName"
```

### 9. Start a Scheduled Task

```powershell
Start-ScheduledTask -TaskName "TaskName"
```

---

## Task Manager

### 10. Open Task Manager

Keyboard shortcut:

```text
Ctrl + Shift + Esc
```

### 11. Processes Investigation

Checked:

* Process Name
* Memory Usage
* Disk Usage
* Network Usage

### 12. Startup Apps Investigation

Checked Startup Apps from a SOC perspective.

**Purpose:** Identify suspicious applications that may be configured to run automatically and potentially provide persistence.

---

## SOC Investigation — Suspicious Service

If an unknown service is discovered, investigate:

1. Who created/installed the service?
2. When was it created?
3. What executable or command does it run?
4. Where is the executable located?
5. Is the executable digitally signed?
6. Is the hash suspicious?
7. Which account is running the service?

---


```
