# JSON request
import sys
from urllib.request import Request, urlopen
from datetime import *
import json


def json_request_error(e):
    print("%s : %s" % (e, datetime.now()), file=sys.stderr)


def json_request(url='', encoding='utf-8',
                 success=None, error=lambda e: print("%s : %s" % (e, datetime.now()), file=sys.stderr)
                 ):
    try:
        resp = urlopen(Request(url))
        if resp.getcode() == 200:
            resp_body = resp.read().decode(encoding)
            resp_json = json.loads(resp_body)

            print('%s: success for request[%s]' % (datetime.now(), url))

            if callable(success) is False:
                return resp_json
            success(resp_json)
    except Exception as e:
        # callable 은 호출이 가능한지 불가능한지의 여부를 확인하는 것이다.
        # 즉, 함수객체인지를 확인한다.
        callable(error) and error('%s %s' % (str(e), url))
