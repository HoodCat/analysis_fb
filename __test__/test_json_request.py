from analysis_fb.collection.api import json_request as jr

url = "http://192.168.1.21:8080/mysite3/api/guestbook/list"
result = jr.json_request(url)
print(result)


def success_fetch_guestbook_list(response):
    print(response)


def error_fetch_guestgbook_list(e, url):
    print('%s : %s' % (e, url))

