from analysis_fb.collection.api import api
import json
url = api.fb_gen_url(node='jtbcnews', a=1, b=2, no=10, token='12345')
print(url)

jtbcnew_id = api.fb_name_to_id('jtbcnews')
print(jtbcnew_id)

# posts = api.fb_fetch_post('jtbcnews', since='2018-05-01', until='2018-05-31')
# print(posts)

for posts in api.fb_fetch_post('jtbcnews', since='2018-05-01', until='2018-05-31'):
    print(posts)
