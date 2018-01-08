#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import tweepy
from secrets import *

print (time.strftime("%I:%M:%S"))
print (time.strftime("%d/%m/%Y"))

# create an OAuthHandler instance

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# construct API instance
api = tweepy.API(auth)

# find tweets that mention @orbital_insight
# follow those users and favorite their tweets

while True:

    for tweet in tweepy.Cursor(api.search, q='@UrtheCast').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@planetlabs').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@DescartesLabs').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@TellusLabs').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@UrsaSpace').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@DJIEnterprise').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='#agribotix').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@agribotix').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@3drobotics').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@orbital_insight').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='#orbitalinsight').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@StructionSite').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='orbital insight').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='orbital insights').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    for tweet in tweepy.Cursor(api.search, q='@autodesku').items(50):
        print tweet.text

        # Print User Name who tweeted
        print '\nTweet by: @' + tweet.user.screen_name
        time.sleep(5)

        # Favorite the tweet

        try:

            tweet.favorite()
            print 'Favorited the tweet'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

            # Follow the user who tweeted

        try:
            tweet.user.follow()
            print 'Followed the user'
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(60)

    print 'made it to the end'
    print (time.strftime("%I:%M:%S"))
    print (time.strftime("%d/%m/%Y"))
    time.sleep(60*60*24)