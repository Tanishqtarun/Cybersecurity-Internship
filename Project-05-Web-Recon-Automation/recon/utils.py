from urllib.parse import urlparse
import re

def normalize_target(target):
    raw = target.strip()
    if not raw.startswith(("http://", "https://")):
        url = "https://" + raw
    else:
        url = raw
    parsed = urlparse(url)
    if not parsed.hostname:
        raise ValueError("Invalid domain or URL")
    host = parsed.hostname.lower().rstrip(".")
    if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        raise ValueError("Unsupported hostname format")
    return host, url

def safe_get(session, url, timeout=10):
    try:
        return session.get(url, timeout=timeout, allow_redirects=True)
    except Exception as exc:
        return None, str(exc)
