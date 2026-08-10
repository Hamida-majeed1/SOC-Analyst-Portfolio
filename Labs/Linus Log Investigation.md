# Linux Log Investigation — SSH Authentication Activity

## 1. Investigation Overview

This investigation focused on analyzing Linux authentication logs to identify suspicious SSH login activity.

The primary log file investigated was:

```bash
/var/log/auth.log
```

The objective was to identify failed login attempts, determine the source IP address and targeted username, and check whether a successful login occurred after multiple failed attempts.

---

## 2. Objective

The objectives of this investigation were:

* Identify failed SSH authentication attempts.
* Identify the targeted username.
* Identify the source IP address.
* Check for successful authentication from the same IP.
* Determine whether the activity was suspicious.
* Provide security recommendations.

---

## 3. Log Source

The authentication log used for the investigation was:

```bash
/var/log/auth.log
```

This log contains authentication-related events such as:

* Successful logins
* Failed login attempts
* SSH authentication activity
* `sudo` activity
* User authentication events

---

## 4. Commands Used

### View Authentication Logs

```bash
cat /var/log/auth.log
```

### Search for Failed SSH Authentication

```bash
grep "Failed password" /var/log/auth.log
```

### Search for Successful Authentication

```bash
grep "Accepted" /var/log/auth.log
```

### Search for Successful Login from a Specific IP

```bash
grep "Accepted" /var/log/auth.log | grep "185.10.20.30"
```

### Count Failed Login Attempts

```bash
grep -i "Failed password" /var/log/auth.log | wc -l
```

### Monitor New Authentication Events in Real Time

```bash
tail -f /var/log/auth.log
```

---

## 5. Investigation Findings

During the investigation, the following failed authentication attempts were identified:

```text
Aug 10 10:15:22 server sshd[1234]: Failed password for admin from 185.10.20.30
Aug 10 10:15:25 server sshd[1235]: Failed password for admin from 185.10.20.30
Aug 10 10:15:28 server sshd[1236]: Failed password for admin from 185.10.20.30
Aug 10 10:15:31 server sshd[1237]: Failed password for admin from 185.10.20.30
```

### Observations

* **Username:** `admin`
* **Source IP:** `185.10.20.30`
* **Failed attempts:** 4
* **Time range:** 10:15:22 – 10:15:31
* **Service:** SSH

The same IP address repeatedly attempted to authenticate using the same username.

---

## 6. Successful Login Investigation

A successful authentication was then identified:

```text
Aug 10 10:16:02 server sshd[1238]: Accepted password for admin from 185.10.20.30
```

The log entry shows:

* **Timestamp:** Aug 10 10:16:02
* **Hostname:** server
* **Authentication:** Accepted password
* **Username:** admin
* **Source IP:** 185.10.20.30

The successful login occurred shortly after multiple failed attempts from the same IP address.

---

## 7. Analysis

The activity is considered **suspicious** because:

1. Multiple failed SSH authentication attempts were observed.
2. All failed attempts originated from the same IP address.
3. The same `admin` account was targeted.
4. A successful login occurred shortly after the failed attempts.
5. The activity is consistent with a **possible brute-force attack that eventually succeeded**.

However, additional investigation would be required to confirm whether the login was actually unauthorized.

---

## 8. Security Recommendations

The following actions are recommended:

* Reset the password for the affected `admin` account if the login is unauthorized.
* Verify whether `185.10.20.30` is an authorized IP address.
* Review other authentication events around the suspicious timestamp.
* Check the system for unauthorized changes or activity.
* Ensure that only authorized users have SSH access.
* Consider using SSH keys instead of password authentication.
* Consider implementing rate limiting or tools such as Fail2ban.
* Review privileged account activity after the successful login.

---

## 9. Conclusion

The investigation identified suspicious SSH authentication activity involving the `admin` account.

Four failed authentication attempts were observed from the IP address `185.10.20.30`, followed shortly by a successful login from the same IP.

This behavior is **consistent with a possible brute-force attack followed by successful authentication**. Further investigation should be performed to determine whether the successful login was authorized.

---

## 10. Skills Demonstrated

This investigation demonstrates the following Linux and SOC analysis skills:

* Linux log analysis
* Authentication log investigation
* SSH log analysis
* `grep`
* `cat`
* `tail`
* `tail -f`
* `wc -l`
* Linux pipes (`|`)
* Identifying failed authentication attempts
* Identifying successful authentication
* IP address investigation
* Username identification
* Timestamp analysis
* Brute-force attack identification
* Basic incident investigation
* Security recommendations
