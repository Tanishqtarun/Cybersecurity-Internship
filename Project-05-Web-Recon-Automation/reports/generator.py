import os, json, html

def write_reports(data, outdir):
    os.makedirs(outdir,exist_ok=True)
    with open(os.path.join(outdir,"reconnaissance.json"),"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,default=str)
    with open(os.path.join(outdir,"reconnaissance.md"),"w",encoding="utf-8") as f:
        f.write(markdown(data))
    with open(os.path.join(outdir,"reconnaissance.html"),"w",encoding="utf-8") as f:
        f.write(html_report(data))

def markdown(d):
    dns=d["dns"]; reg=d["registration"]; geo=d["ip_geolocation"]; ssl=d["ssl_tls"]
    lines=[f"# Web Reconnaissance Report: {d['target']}",
           "", "## Scope", "Passive/public-data reconnaissance only. No exploitation or intrusive scanning was performed.", "",
           "## Summary", f"- IP: {geo.get('ip','N/A')}", f"- HTTP status: {d['http'].get('status_code','N/A')}",
           f"- Final URL: {d['http'].get('final_url','N/A')}", "",
           "## DNS Records"]
    for k in ["A","AAAA","MX","NS","TXT","CNAME"]:
        lines.append(f"- **{k}:** {', '.join(dns.get(k,[])) or 'None observed'}")
    lines += ["","## Registration / RDAP",f"- Source: {reg.get('source') or 'Unavailable'}",
              f"- Creation: {reg.get('events',{}).get('registration','N/A')}",
              f"- Expiry: {reg.get('events',{}).get('expiration','N/A')}",
              f"- Nameservers: {', '.join(reg.get('nameservers',[])) or 'Unavailable'}","",
              "## SSL/TLS",f"- Enabled: {ssl.get('enabled')}",f"- TLS version: {ssl.get('tls_version','N/A')}",
              f"- Valid from: {ssl.get('not_before','N/A')}",f"- Valid until: {ssl.get('not_after','N/A')}","",
              "## robots.txt / sitemap.xml"]
    for k,v in d["web_files"].items():
        lines.append(f"- **{k}:** {'available' if v.get('available') else 'not available'}")
    lines += ["","## Basic Security Observations"]
    for x in d["security_observations"]["observations"]:
        lines.append(f"- {x}")
    if not d["security_observations"]["observations"]: lines.append("- No observations from the selected passive checks.")
    lines += ["","## Limitations","Results depend on public DNS/RDAP data and the target's current HTTP/TLS configuration."]
    return "\n".join(lines)+"\n"

def html_report(d):
    md=markdown(d)
    body=html.escape(md).replace("\n","<br>")
    return f"""<!doctype html><html><head><meta charset='utf-8'><title>Recon Report - {html.escape(d['target'])}</title>
<style>body{{font-family:Arial,sans-serif;max-width:900px;margin:40px auto;line-height:1.6}}h1{{color:#17324d}}.box{{padding:20px;border:1px solid #ddd;border-radius:8px}}</style></head>
<body><div class='box'><h1>Web Reconnaissance Report</h1><div>{body}</div></div></body></html>"""
