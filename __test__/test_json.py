# JSON testing
import sys
from urllib.request import Request, urlopen
from datetime import *
import json

try:
    url = "http://192.168.1.21:8080/mysite3/api/guestbook/list"

    request = Request(url)
    resp = urlopen(request)

    resp_body = resp.read().decode('UTF-8')
    d = json.loads(resp_body)
    for key, value in d.items():
        print(key, value, sep='|')
except Exception as e:
    print('%s: %s' % (e, datetime.now()), file=sys.stderr)
