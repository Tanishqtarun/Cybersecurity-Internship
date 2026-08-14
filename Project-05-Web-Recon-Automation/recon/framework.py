import requests
from .utils import normalize_target
from .dns import collect_dns
from .http import collect_http, collect_robots_and_sitemap
from .ssl_info import collect_ssl
from .whois_rdap import collect_registration
from .geo import collect_ip_geo
from .security import assess_headers

def run_recon(target):
    domain, url=normalize_target(target)
    session=requests.Session()
    http=collect_http(url)
    base=http.get("final_url") or url
    result={
        "target":domain,
        "http":http,
        "dns":collect_dns(domain),
        "ip_geolocation":collect_ip_geo(domain),
        "registration":collect_registration(domain),
        "ssl_tls":collect_ssl(domain),
        "web_files":collect_robots_and_sitemap(base),
    }
    result["security_observations"]=assess_headers(http.get("headers",{}))
    return result
