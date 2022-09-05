import datetime, tweepy, json  #Block1
from datetime import datetime, timedelta, timezone

consumer_key = 'XXXXXX'     #Block2
consumer_secret = 'XXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXXXXXX'

api = tweepy.Client(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret, wait_on_rate_limit = True)

end_date = datetime.now(timezone.utc) - timedelta(days = 2000)
print('end_date = ', end_date)
start_date = datetime.now(timezone.utc) - timedelta(days = 2365)
print('start_date = ', start_date)  #Block4

fp = open("C:/Users/LA/UBICACIÓN/DEL/ARCHIVO/tweet.js","r", encoding='UTF-8')
myjson = json.load(fp)  #Block 5

trash_tweet_ids = [] #Block6
for tweet in myjson:
   d = datetime.strptime(tweet['tweet']['created_at'], "%a %b %d    %H:%M:%S %z %Y")
   if d > start_date and d < end_date:
     trash_tweet_ids.append(tweet['tweet']['id_str'])
     try:
         api.delete_tweet(tweet['tweet']['id_str'], user_auth = True)
         print(tweet['tweet']["created_at"] + " " + tweet['tweet'] ['id_str'] + ' deleted successfully')
     except Exception as e: 
         print('error', e)
         pass
print(str(len(trash_tweet_ids)) + ' trash tweets have been deleted…')
