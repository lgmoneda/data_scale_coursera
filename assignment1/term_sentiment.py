import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] = int(score)
    #print scores.items()

    tweets = {}
    i = 0
    for tweet in tweet_file:
    	tweets[i] = json.loads(tweet) 
    	score_sum = 0
    	ntweet = tweets[i].get("text", " ")
    	#print ntweet
    	for word in ntweet.split():
    		#print "Palavra: " + word
    		score_sum += scores.get(word, 0) 
    	#print int(score_sum)
    	for word in ntweet.split():
    		if scores.get(word, 0) == 0:
    			scores[word] = float(score_sum/len(ntweet))
    			print word + " " + str(scores[word])
    			#sys.stdout.write(str(word + " " + str(scores[word]) + "\n"))
    	#sys.stdout.write(str(score_sum) + '\n')
    	i+=1

    #for term, score in scores:
    #	print term + " " + float(score)

if __name__ == '__main__':
    main()
