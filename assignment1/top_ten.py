import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    tweets = {}
    freq_dic = {}
    total_words = 0
    i = 0
    for tweet in tweet_file:
    	tweets[i] = json.loads(tweet) 
    	ntweet = tweets[i].get("entities", " ")
        if ntweet != " ":
            for hashtag in ntweet.get("hashtags", " "):
                total_words+=1
                freq_dic[hashtag["text"]] = freq_dic.get(hashtag["text"], 0) + 1 
    	i+=1

    sorted_freq = sorted(freq_dic.items(), key=operator.itemgetter(1), reverse=True)
    for word, freq in sorted_freq[0:10]:
        print word + " " + str(freq)


if __name__ == '__main__':
    main()
