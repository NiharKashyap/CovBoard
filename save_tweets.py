import pandas as pd
from csv import writer

#tweet_csv = pd.read_csv('tweets.csv')

def save(list):
	df = pd.DataFrame(list)
	df.to_csv('tweet_cleaned.csv', mode='a', index=False, header=False)

