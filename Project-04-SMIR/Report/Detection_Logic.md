# Detection Logic

## Objective

Identify suspicious authentication attempts that may indicate unauthorized access or brute-force attacks.

---

## Detection Indicators

The following indicators were used during analysis:

- Multiple failed SSH login attempts
- Invalid username authentication attempts
- Repeated authentication failures from the same IP address
- High number of login attempts within a short period
- SSH session termination due to excessive authentication failures

---

## Observed Indicators

| Indicator | Status |
|-----------|--------|
| Multiple Failed Logins | Detected |
| Invalid User Attempts | Detected |
| Repeated Source IP | Detected |
| Username Enumeration | Detected |
| Too Many Authentication Failures | Detected |

---

## Detection Method

The authentication logs were manually reviewed to identify suspicious login behavior. Events were correlated based on:

- Timestamp
- Source IP Address
- Username
- Authentication Result

---

## Conclusion

The collected evidence indicates a brute-force attack attempting to gain unauthorized SSH access using multiple commonly known usernames.

## Additional Detection Rules

### Rule 1 – Login from Unusual Location

Trigger an alert if a user logs in from an IP address or geographic location that has not been previously associated with the account.

Reason:
This may indicate compromised credentials.

---

### Rule 2 – Administrative Login Outside Business Hours

Trigger an alert whenever an administrator logs in outside normal business hours (e.g., 8 PM–6 AM).

Reason:
Unexpected administrative activity may indicate unauthorized access.

---

### Rule 3 – Repeated Failed Authentication Attempts

Trigger an alert if more than five failed SSH login attempts occur from the same IP address within five minutes.

Reason:
This behavior is commonly associated with brute-force attacks.