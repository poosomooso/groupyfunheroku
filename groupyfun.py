#import groupy
import requests, urllib2

# groups = groupy.Group.list()
# print(groups)
# bots = groupy.Bot.list()[0]
# print(bots)
# bots.post('snails are a lie')

link = 'https://en.wikipedia.org/wiki/Special:Random'

page = urllib2.urlopen(link).geturl()

body = {'bot_id': '335cd8afefe1251ead5f495127', 'text': 'Daily Reminder that you\'re gross: '+link, 'token':'INMXfur7OSiUV9JTbHhRBb045LHRLSkU23HQoU5D'}

# Make the POST request here, passing body as the data:
response = requests.post('https://api.groupme.com/v3/bots/post/', data=body)