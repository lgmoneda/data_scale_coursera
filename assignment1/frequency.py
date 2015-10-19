import sys
import json

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
    	ntweet = tweets[i].get("text", " ")
    	#print ntweet
    	for word in ntweet.split():
            total_words+=1
            freq_dic[word] = freq_dic.get(word, 0) + 1 
    	i+=1

    for word, freq in freq_dic.iteritems():
        print word + " {0:.16f}".format(float(freq/total_words)) 

    #for term, score in scores:
    #	print term + " " + float(score)

if __name__ == '__main__':
    main()
