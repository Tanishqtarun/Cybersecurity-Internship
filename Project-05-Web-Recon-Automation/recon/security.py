SECURITY_HEADERS={
    "content-security-policy":"CSP",
    "strict-transport-security":"HSTS",
    "x-frame-options":"X-Frame-Options",
    "x-content-type-options":"X-Content-Type-Options",
    "referrer-policy":"Referrer-Policy",
    "permissions-policy":"Permissions-Policy",
}

def assess_headers(headers):
    lower={k.lower():v for k,v in headers.items()}
    missing=[label for key,label in SECURITY_HEADERS.items() if key not in lower]
    observations=[]
    if missing: observations.append("Missing security headers: " + ", ".join(missing))
    server=lower.get("server")
    if server: observations.append(f"Server header exposed: {server}")
    powered=lower.get("x-powered-by")
    if powered: observations.append(f"Technology banner exposed: {powered}")
    return {"missing_headers":missing,"observations":observations}
