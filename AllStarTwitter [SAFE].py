import random, tweepy, time
from lyrics import LYRICS

def getTweet():
    return(random.choice(LYRICS))


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    cfg = {
    "consumer_key"          : "",     #these have been removed for security reasons
    "consumer_secret"       : "",     #ensure you enter your correct tokens and keys
    "access_token"          : "",     #for the bot to work
    "access_token_secret"   : ""
    }
    api = get_api(cfg)

    while True:
        try:
            finTweet = getTweet()
            status = api.update_status(status=finTweet)
        except:
             continue
        else:
            break
    time.sleep(3600)
    main()

if __name__ == "__main__":
    main()
