
#df = pd.read_csv('tweet_csv.csv')

class CleanTweet:

	def __init__(self):
		self.numbers ='''0123456789'''

	def clean(self, line):
		num = []
		str= ''
		for words in line:
			if(words in self.numbers):
				str = str + words
			else:
				if(len(str)!=0):
					num.append(str)
				str = ''
		print(num)
		return num
