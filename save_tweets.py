import pandas as pd

#tweet_csv = pd.read_csv('tweets.csv')

def save(list):
	df = pd.DataFrame(list)
	df.to_csv('tweet_cleaned.csv')

