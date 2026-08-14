import requests

def collect_registration(domain):
    """Uses public RDAP where available; no account/API key required."""
    urls=[
        f"https://rdap.org/domain/{domain}",
        f"https://rdap.verisign.com/com/v1/domain/{domain}",
    ]
    for url in urls:
        try:
            r=requests.get(url,timeout=12,headers={"User-Agent":"Project05-WebRecon/1.0"})
            if r.ok:
                data=r.json()
                events={}
                for e in data.get("events",[]):
                    events[e.get("eventAction","unknown")]=e.get("eventDate")
                nameservers=[x.get("ldhName") for x in data.get("nameservers",[]) if x.get("ldhName")]
                return {"source":url,"handle":data.get("handle"),"status":data.get("status",[]),
                        "events":events,"nameservers":nameservers,"error":None}
        except Exception:
            pass
    return {"source":None,"handle":None,"status":[],"events":{},"nameservers":[],"error":"RDAP data unavailable"}
