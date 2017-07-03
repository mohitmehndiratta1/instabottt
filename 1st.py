import requests

APP_ACCESS_TOKEN = '1678122958.1677ed0.24eead1a2d05411093589d9da13255a2'
#access token for self info

BASE_URL = 'https://api.instagram.com/v1/'


def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  #convert json into py

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'User does not exist!'
        #no user found
  else:
    print 'Status code other than 200 received!'

self_info()