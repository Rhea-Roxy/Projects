import tweepy

CONSUMER_KEY = 'P4w7A1woQ68edBXiFNvy9NSaV'
CONSUMER_SECRET = '2z6LkCxpaQ4X5l3x6Q2d7yfo1FNEbLqOvxXHh2mw3VnuB4OIyQ'
ACCESS_KEY = '1489092358281089027-TsRk9KujhYcKRINEJMUnyS3kJDgiDM'
ACCESS_SECRET = 'f9Y83mcU9qXpRlbdhQPV0wXMlv2IjhATRGw3aFecI7AJu'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'hello.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


# if the id of the last seen is supplied to Tweets then it will reply only to the last one

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# tweet_mode cannot be used cause tweepy updated it
last_seen_id = read_last_seen(FILE_NAME)
tweets = api.mentions_timeline(since_id=last_seen_id, tweet_mode='extended')

for tweet in reversed(tweets):
    if '#newbot' in tweet.full_text.lower():
        print(str(tweet.id) + ' - ' + tweet.full_text)
        api.update_status(status ="@"+tweet.user.screen_name + " Auto reply works: ", in_reply_to_status_id =tweet.id)
        store_last_seen(FILE_NAME, tweet.id)
