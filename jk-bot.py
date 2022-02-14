# import necessary libraries
import tweepy
import configparser
from time import sleep


# provision for credentials
config = configparser.ConfigParser()
config.read('config.ini')

apiKey = config['jk_bot']['apiKey']
apiKeySecret = config['jk_bot']['apiKeySecret']

accessToken = config['jk_bot']['accessToken']
accessTokenSecret = config['jk_bot']['accessTokenSecret']


# authenticate API keys 
auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
print('Authentication successful!')

api = tweepy.API(auth)


# assign to favorite and follow
Favorite = True
Follow = True

hashtags = ['#python']

# the function with the logic on the bot actions
def main():
    for tweet in tweepy.Cursor(
        api.search_tweets, q=hashtags).items():
        try:
            print("\nTweet by: @" + tweet.user.screen_name)
            
            # check if we have retweeted and retweet if not
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                    print("Tweet retweeted!")
                except Exception as e:
                    print(e)

            # check if we have favorited and favorite if not
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    print("Tweet favorited!")
                except Exception as e:
                    print(e)
            # # retweet
            # tweet.retweet()
            
            # # favorite
            # if Favorite:
            #     tweet.favorite()
                
            # # follow if true, and if not following
            # if Follow and not tweet.user.following:
            #     tweet.user.follow()
                
            # bot sleep time (seconds)
            sleep(60)
            
        except tweepy.TweepyError as e:
            print(e.reason)
            
            
        except StopIteration:
            break
        
        
while True:
    main()
    sleep(20)
    
# TODO:
# check for tweets already retweeted

       
# TODO:- implement using tweepy Stream rather than search (Below is my attempt);
# # create class to read tweets in real time
# class Listener(tweepy.Stream):
#     # create a function to get the status==tweet
#     def on_status(self, status):
#         print("Successfully retweeted tweet from:" '-' + status.user.screen_name)
          
# stream_tweet = Listener(apiKey, apiKeySecret, accessToken, accessTokenSecret)

# keywords = ["#python"]

# # filter realtime Tweets by keywords
# stream_tweet.filter(track=keywords)