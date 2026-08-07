## Incident Response Workflow

### 1. Detection

The security monitoring process identified multiple failed SSH authentication attempts originating from IP address 198.51.100.23.

### 2. Alert

Repeated authentication failures triggered a security alert indicating a potential brute-force attack.

### 3. Investigation

Authentication logs were reviewed to identify the source IP, targeted usernames, attack timeline, and authentication outcomes.

### 4. Response

The suspicious IP address should be blocked using firewall rules or Fail2Ban. Password authentication should be reviewed, and affected accounts monitored.

### 5. Recovery

Verify system integrity, rotate credentials if necessary, apply security updates, and continue monitoring for additional malicious activity.

### 6. Closure

The incident is documented, mitigation measures are implemented, and recommendations are provided to reduce the risk of future attacks.