import tweepy
import credentials
import save_tweets as st
#import clean
from clean import CleanTweet
import datetime
from save_to_sheet import Gsheet

cleant = CleanTweet()

gs = Gsheet()


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

date_since = datetime.datetime.now().date()

tweets = tweepy.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items()
output = []
for tweet in tweets:

    line = {'Date':str(tweet.created_at), 'Count':cleant.clean(tweet.text)}
    output.append(line)
    print(tweet.created_at)
    print('\n')
    print(tweet.text)
    print('\n')

#st.save(output)
gs.save_sheet(output)