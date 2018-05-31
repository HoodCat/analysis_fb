# facebook api
from urllib.parse import urlencode
from .json_request import json_request

LIMITS_REQUEST=50
BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'
ACCESS_TOKEN = 'EAACEdEose0cBACJTGfnwhmhqbJmp7SY4lyhN8JPGKHkgZB8miNisArsoqLXoSfEPguPWmx5HY4UZC0D43TGI20IoV4VcZBiVRoAkLpbHTuZBxf9Rz4CJiSjpnlGox51xczp9bTi3qLZBjpdZAR3xWmVXitkBdToidhfO8QZAipRnScWuIBNntH96u0UTdK1j19GLDOEZA01gZBwZDZD'


def fb_gen_url(base=BASE_URL_FB_API, node='', **param):
    return '%s/%s/?%s' % (base, node, urlencode(param))


def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url)
    return json_result.get('id')


def fb_fetch_post(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + '/posts',
        fields='id,message,link,name,type,shares,created_time,'
               'reactions.limit(0).summary(true),'
               'comments.limit(0).summary(true)',
        since=since,
        until=until,
        limit=LIMITS_REQUEST,
        access_token=ACCESS_TOKEN
    )
    is_next = True
    data = []
    while is_next:
        json_result = json_request(url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get('next')
        is_next = url is not None

    yield posts

