# Incident Classification

## Incident Summary

During log analysis, multiple failed SSH authentication attempts were identified originating from the IP address **198.51.100.23**. The attacker attempted to authenticate using several common usernames, including `admin`, `postgres`, `database`, `oracle`, `support`, `pi`, `test`, and `www-data`.

The repeated authentication failures indicate an automated brute-force attack targeting the SSH service.

---

## Incident Type

- Brute Force Attack
- Unauthorized Access Attempt
- Username Enumeration

---

## Severity

**Critical**

---

## Affected Service

- SSH (Secure Shell)

---

## Source IP Address

198.51.100.23

---

## Evidence

The following activities were observed in the authentication logs:

- Multiple "Invalid user" entries
- Numerous "Failed password" attempts
- Authentication attempts against several usernames
- "Too many authentication failures" message
- Repeated activity from the same IP address

---

## Impact Assessment

Although no successful authentication was identified in the provided logs, the attack could have resulted in unauthorized access if weak credentials had been used.

Potential impacts include:

- Unauthorized system access
- Privilege escalation
- Data theft
- Service disruption

---

## Incident Status

Attack Detected

No evidence of successful compromise was identified in the provided authentication logs.