# Architecture Note

## 1. Overview

The Web Recon Automation Framework follows a modular architecture in which the main program coordinates multiple independent reconnaissance collectors.

The framework accepts a target domain or URL, collects publicly available information, performs basic security observations, and generates structured reports.

## 2. Architecture Flow

```text
                    Target Domain / URL
                           |
                           v
                      CLI Input
                           |
                           v
                    Main Controller
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       RDAP/WHOIS        DNS           Web/HTTP
       Collector       Collector       Collector
          |                |                |
          |                |                +--> HTTP Headers
          |                |                +--> robots.txt
          |                |                +--> sitemap.xml
          |                |
          |                +--> A / AAAA
          |                +--> MX / NS
          |                +--> TXT / CNAME
          |
          +--> Registration
          +--> Expiry
          +--> Nameservers

                           |
          +----------------+----------------+
          |                |                |
          v                v                v
     IP / Geo           SSL/TLS       Security Checks
     Information        Details       & Observations
          |                |                |
          +----------------+----------------+
                           |
                           v
                    Structured Results
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
         JSON           Markdown          HTML