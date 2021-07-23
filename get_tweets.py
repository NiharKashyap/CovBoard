import tweepy
import credentials
import save_tweets as st
#import clean
from clean import CleanTweet
from datetime import date

cleant = CleanTweet()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


#userID = "DeputyJorhat"
#userID = "Deputy Commissioner, Jorhat"


new_search = "COVID Update from:DeputyJorhat"

#date_since = "2021-07-01"

date_since = date.today()

tweets = tweepy.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(5)
output = []
for tweet in tweets:

    line = {'date':tweet.created_at, 'text':cleant.clean(tweet.text)}
    output.append(line)
    print(tweet.created_at)
    print('\n')
    print(tweet.text)
    print('\n')

st.save(output)
