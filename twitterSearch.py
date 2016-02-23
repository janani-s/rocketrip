import argparse
import tweepy
from tweepy import OAuthHandler

parser = argparse.ArgumentParser(prog='Twitter Search')
parser.add_argument('-ck', '--consumer_key', dest='consumer_key', required=True, help='Twitter application consumer key')
parser.add_argument('-cs', '--consumer_secret', dest='consumer_secret', required=True, help='Twitter application consumer secret')
parser.add_argument('-at', '--access_token', dest='access_token', required=True, help='Twitter application access token')
parser.add_argument('-as', '--access_secret', dest='access_secret', required=True, help='Twitter application access secret')
parser.add_argument('-k', '--keyword', dest='keyword', required=True, help='Keyword to search in tweets')

args = parser.parse_args()

auth = OAuthHandler(args.consumer_key, args.consumer_secret)
auth.set_access_token(args.access_token, args.access_secret)

api = tweepy.API(auth)
results = api.search(q=args.keyword)

for result in results:
    print '@' + result.author.screen_name + ':' + result.text
    if(result.entities["urls"]):
        print 'Media:' + result.entities["urls"][0]["expanded_url"]
    break