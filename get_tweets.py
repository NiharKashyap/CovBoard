import tweepy
import credentials

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

date_since = "2021-07-01"

tweets = tweepy.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(5)

for tweet in tweets:
	print(tweet.created_at)
	print('\n')
	print(tweet.text)
	print('\n')
