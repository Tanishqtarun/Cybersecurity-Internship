import socket, ssl
from datetime import datetime, timezone

def collect_ssl(domain, port=443):
    out={"enabled":False,"error":None}
    ctx=ssl.create_default_context()
    try:
        with socket.create_connection((domain,port),timeout=8) as sock:
            with ctx.wrap_socket(sock,server_hostname=domain) as ssock:
                cert=ssock.getpeercert()
                out["enabled"]=True
                out["issuer"]=dict(x[0] for x in cert.get("issuer",[]))
                out["subject"]=dict(x[0] for x in cert.get("subject",[]))
                out["not_before"]=cert.get("notBefore")
                out["not_after"]=cert.get("notAfter")
                out["tls_version"]=ssock.version()
                out["cipher"]=ssock.cipher()
    except Exception as exc:
        out["error"]=str(exc)
    return out
