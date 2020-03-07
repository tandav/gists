import sys
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def clean(url, allowed_params=('q', 'tbm')):
    o = urlparse(url)
    params = parse_qs(o.query)
    clean_params = {p: params[p] for p in allowed_params}
    clean_url = urlunparse(o._replace(query=urlencode(clean_params, doseq=True)))
    return clean_url

print(clean(sys.argv[1]))
