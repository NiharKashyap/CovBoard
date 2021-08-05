This program fetches daily covid cases of Jorhat district situated in Assam, India from twitter. 

I have hosted the script on PythonAnywhere. It will run every night at 11:47 PM
and update a google sheet with new data if there is any. Along with the script
there is a single page website with a Flask server hosted in PythonAnywhere. It
will serve a HTML page to users requesting the url. The HTML page has an embedded
Dashboard made using Google Data Studio.

It will show 5 things:

1. Daily cases detected
2. Daily cases active
3. Daily Deaths
4. Highest single day spike
5. Highest single day deaths


The only downside is that since I am scraping the data from twitter there
won't be any update for a particular day if the user does not tweet.

You can chekout the website here: http://namelesswonder.pythonanywhere.com

NB: I have not upladed the credentials file since GitGuardian won't allow me
and I don't want to get hacked. If you clone this repo make sure to add a
credentials.py file with you twitter consumer_key, consumer_secret, 
access_token and access_token_secret
