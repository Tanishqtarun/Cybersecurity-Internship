import socket, requests

def collect_ip_geo(domain):
    try:
        ip=socket.gethostbyname(domain)
    except Exception as exc:
        return {"ip":None,"error":str(exc)}
    out={"ip":ip}
    try:
        r=requests.get(f"https://ipapi.co/{ip}/json/",timeout=8,
                       headers={"User-Agent":"Project05-WebRecon/1.0"})
        if r.ok:
            d=r.json()
            for k in ["city","region","country_name","latitude","longitude","org","asn"]:
                out[k]=d.get(k)
        else:
            out["geo_error"]=f"HTTP {r.status_code}"
    except Exception as exc:
        out["geo_error"]=str(exc)
    return out
