import random, tweepy, time

def getTweet():
    lyrics = ['Somebody once told me the world is gonna roll me' , 'I ain\'t the sharpest tool in the shed' , 'She was looking kind of dumb with her finger and her thumb' , 'In the shape of an "L" on her forehead' , 'Well the years start coming and they don\'t stop coming' , 'Fed to the rules and I hit the ground running' , 'Didn\'t make sense not to live for fun' , 'Your brain gets smart but your head gets dumb' , 'So much to do, so much to see' , 'So what\'s wrong with taking the back streets?' , 'You\'ll never know if you don\'t go' , 'You\'ll never shine if you don\'t glow' , 'Hey now, you\'re an all-star, get your game on, go play' , 'Hey now, you\'re a rock star, get the show on, get paid' , 'And all that glitters is gold' , 'Only shooting stars break the mold' , 'It\'s a cool place and they say it gets colder' , 'You\'re bundled up now, wait till you get older' , 'But the meteor men beg to differ' , 'Judging by the hole in the satellite picture' , 'The ice we skate is getting pretty thin' , 'The water\'s getting warm so you might as well swim' , 'My world\'s on fire, how about yours?' , 'That\'s the way I like it and I never get bored' , 'Hey now, you\'re an all-star, get your game on, go play' , 'Hey now, you\'re a rock star, get the show on, get paid' , 'All that glitters is gold' , 'Only shooting stars break the mold' , 'Hey now, you\'re an all-star, get your game on, go play' , 'Hey now, you\'re a rock star, get the show, on get paid' , 'And all that glitters is gold' , 'Only shooting stars' , 'Somebody once asked could I spare some change for gas?' , 'I need to get myself away from this place' , 'I said yep what a concept' , 'I could use a little fuel myself' , 'And we could all use a little change' , 'Well, the years start coming and they don\'t stop coming' , 'Fed to the rules and I hit the ground running' , 'Didn\'t make sense not to live for fun' , 'Your brain gets smart but your head gets dumb' , 'So much to do, so much to see' , 'So what\'s wrong with taking the back streets?' , 'You\'ll never know if you don\'t go (go!)' , 'You\'ll never shine if you don\'t glow' , 'Hey now, you\'re an all-star, get your game on, go play' , 'Hey now, you\'re a rock star, get the show on, get paid' , 'And all that glitters is gold' , 'Only shooting stars break the mold' , 'And all that glitters is gold' , 'Only shooting stars break the mold']
    return(lyrics[random.randrange(1, 50)])


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
            time.sleep(3600)
            main()
            break

if __name__ == "__main__":
    main()
