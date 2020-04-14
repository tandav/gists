import sys
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def clean(url, allowed_params=('q', 'tbm')):
    o = urlparse(url)
    params = parse_qs(o.query)
    clean_params = {p: params[p] for p in params.keys() & allowed_params}
    clean_url = urlunparse(o._replace(query=urlencode(clean_params, doseq=True)))
    
    # drop https:// scheme part
    clean_url = clean_url.partition('google.com')
    clean_url = ''.join(clean_url[1:])
    
    return clean_url

print(clean(sys.argv[1]))
