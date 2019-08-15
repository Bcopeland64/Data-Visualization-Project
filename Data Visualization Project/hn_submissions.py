#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HO0me
#
# Created:     23/04/2019
# Copyright:   (c) HO0me 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests

from operator import itemgetter

#Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'
r = requests.get(url)
print("Status Code:", r.status_code)

#Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'Title': response_dict['title'],
        'Link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'Comments': response_dict.get('descendents', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print("Discussion Link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

