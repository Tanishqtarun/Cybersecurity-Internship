# Project 05 - Web Recon Automation Framework

A modular, passive web reconnaissance framework for collecting publicly available information about a domain or URL that you are authorized to assess.

## Features
- RDAP-based domain registration information
- DNS A, AAAA, MX, NS, TXT and CNAME records
- IP address and basic geolocation
- HTTP response headers and status
- SSL/TLS certificate details
- robots.txt and sitemap.xml
- Basic security-header observations
- Graceful error handling
- Markdown, HTML and JSON report generation

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python main.py example.com
```
Replace `example.com` with a domain/URL you are authorized to assess.

## Output
Reports are created under `reports/output/`:
- reconnaissance.json
- reconnaissance.md
- reconnaissance.html

## Architecture
`main.py` handles CLI input and orchestration. Each collector has one responsibility. `framework.py` coordinates collectors. `reports/generator.py` converts the collected structured data into human-readable reports.

## Limitations
This project performs passive/public-data reconnaissance only. It does not brute-force, exploit, crawl aggressively, port-scan, or attempt authentication.
