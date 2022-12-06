import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#whyididntreport OR #IDidNotReport OR #ididnotreport OR #IDidntReport OR #ididntreport OR #WhyIDidNotReport) until:2022-10-31 since:2020-01-01"
tweets = []
limit = 50


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

    print(vars(tweet))
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('whyididntreport_tweets.csv')