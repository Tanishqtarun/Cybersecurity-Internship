# Web Reconnaissance Report: example.com

## Scope
Passive/public-data reconnaissance only. No exploitation or intrusive scanning was performed.

## Summary
- IP: 104.20.23.154
- HTTP status: 200
- Final URL: https://example.com/

## DNS Records
- **A:** 104.20.23.154, 172.66.147.243
- **AAAA:** 2606:4700:10::ac42:93f3, 2606:4700:10::6814:179a
- **MX:** 0 .
- **NS:** elliott.ns.cloudflare.com., hera.ns.cloudflare.com.
- **TXT:** v=spf1 -all, _k2n1y4vw3qtb4skdx9e7dxt97qrmmq9
- **CNAME:** None observed

## Registration / RDAP
- Source: https://rdap.org/domain/example.com
- Creation: 1995-08-14T04:00:00Z
- Expiry: 2027-08-13T04:00:00Z
- Nameservers: ELLIOTT.NS.CLOUDFLARE.COM, HERA.NS.CLOUDFLARE.COM

## SSL/TLS
- Enabled: True
- TLS version: TLSv1.3
- Valid from: Jul 29 22:10:08 2026 GMT
- Valid until: Oct 27 22:17:21 2026 GMT

## robots.txt / sitemap.xml
- **robots_txt:** not available
- **sitemap_xml:** not available

## Basic Security Observations
- Missing security headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy
- Server header exposed: cloudflare

## Limitations
Results depend on public DNS/RDAP data and the target's current HTTP/TLS configuration.
