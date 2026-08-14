import requests

def collect_http(url):
    result={"final_url":None,"status_code":None,"headers":{},"error":None}
    try:
        r=requests.get(url, timeout=10, allow_redirects=True, headers={"User-Agent":"Project05-WebRecon/1.0"})
        result["final_url"]=r.url
        result["status_code"]=r.status_code
        result["headers"]=dict(r.headers)
    except Exception as exc:
        result["error"]=str(exc)
    return result

def collect_robots_and_sitemap(base_url):
    out={}
    for name,path in [("robots_txt","/robots.txt"),("sitemap_xml","/sitemap.xml")]:
        try:
            r=requests.get(base_url.rstrip("/") + path, timeout=10, allow_redirects=True,
                           headers={"User-Agent":"Project05-WebRecon/1.0"})
            out[name]={"status_code":r.status_code,"content":r.text[:20000],
                       "url":r.url,"available":r.status_code==200}
        except Exception as exc:
            out[name]={"available":False,"error":str(exc)}
    return out
