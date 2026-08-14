def collect_dns(domain):
    data = {"A": [], "AAAA": [], "MX": [], "NS": [], "TXT": [], "CNAME": [], "errors": []}
    try:
        import dns.resolver
    except ImportError:
        data["errors"].append("dnspython is not installed")
        return data
    for rtype in ["A","AAAA","MX","NS","TXT","CNAME"]:
        try:
            answers = dns.resolver.resolve(domain, rtype, lifetime=5)
            for a in answers:
                data[rtype].append(str(a).strip('"'))
        except Exception as exc:
            data["errors"].append(f"{rtype}: {exc}")
    return data
