# read line.
# get freg.  
# remove stop words from the line. 
# tell where the words comes from.
# word, freg, cat.
# check if
import re
import collections
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

FILENAME = "emoji_tweets_sentence_tweets_categorisation.txt"
NEGATIVE = ['fuck','bolaya','jealous','shit','bad','unpleasant', 'worse','sucks','suck']
POSITIVE = ['love','like','best','better','lovely','amazing','great','greatest']
NATIVE_WORD_STOP = ['ga', 'se', 'mo', 'gore', 'jo', 'be','ke', 'ka', 're', 'e']

# get frequency of words
def getFreq1( data ):
  res = {}
  for i in data.split(" "):
    if i in res.keys():
      res[ i ] += 1
    else:
      res[i] = 1
  return res

# get frequency of words
def getFreq( data ):
  data = clean( data )
  res = {}
  for i in data.split(" "):
    if i in res.keys():
      res[ i ] += 1
    else:
      res[i] = 1
  return res

# read data by lines
def readLines():
  data = ""
  with open( FILENAME, "r", encoding="utf8" ) as obj: 
    data = obj.readlines()
  return data

#
def sortByValue( data ):
  d = sorted( data.items(), key = lambda item: item[1], reverse=True )
  return d


# sort dict with array as value 
def sortByValueArr( data ):
  d = sorted( data.items(), key = lambda item: item[1][0], reverse=True )
  return d

# read data by
def read( FILENAME="emoji_tweets_sentence_tweets_categorisation.txt" ):
  data = ""
  with open( FILENAME, "r", encoding="utf8" ) as obj: 
    data = obj.read()
  data = ' '.join( data.split() )
  return data

# clean the data
def clean( data ):
  # exceot this chars.
  data = re.sub("[^\sa-z0-9]", "", data.lower() )
  data = re.sub("neutral", "", data.lower() )
  data = re.sub("positive", "", data.lower() )
  data = re.sub("negative", "", data.lower() )
  data = ' '.join( data.split() )
  return data

# clean the data without removing data
def clean1( data ):
  # exceot this chars.
  data = re.sub("[^\sa-z0-9]", "", data.lower() )
  data = ' '.join( data.split() )
  return data

# get words with freq >= 50
def filterMoreThanFreq( data ):
  d = []
  for item in data:
    if item[1] >= 100:
      d.append( item ) 
  return d     
 
# get words from a category
def getCat( data, cat ):
  return [ item for item in data if item[2] == cat ]

# remove stop words from frequency codes
def removeStopWords( data ):
  stop_words = set(stopwords.words('english'))
  tokens = word_tokenize( data )
  stop_words = list( stop_words ) + NATIVE_WORD_STOP
  d = [ word for word in tokens if not word.lower() in stop_words ]
  return ' '.join( d )

# add category to word freq
def addCat( data ):
  d = []
  for item in data:
    if item[0] in POSITIVE:
      d.append( (item[0], item[1], 'positive') )
    elif item[0] in NEGATIVE:
      d.append( (item[0], item[1], 'negative') )
    else:
      d.append( (item[0], item[1], 'neutral') )
  return d
  
# add category to word freq, using the
def addCat1( data, label ):
  d = []
  for item in data:
    d.append( (item[0], item[1], label) )
  return d  

# add categeory to tweet, based on the word category.
def addCatTweet( tweets, data ):
  d = []
  for tweet in tweets:
    if len( clean( tweet ) ) > 0: 
      freg = 0; cat = ''; l = []
      for item in data:
        if item[0] in tweet and item[1] > freg:
          cat = item[2]
          l.append( item )
      tweet = clean( tweet )
      length = len(tweet.split(' '))
      
      if len( l ) > 2:
        first = l[:2][0][2]; second = l[:2][1][2]
        # print( "here...", first,  second )
        if first == 'neutral' and second == "neutral":
          d.append( f"{tweet} | there atleast is 2 neutral words in a sentence of {length} **{cat}**" )
        elif l[:2][0][2] == 'positive' and l[:2][1][2] == "neutral" or l[:2][0][2] == 'neutral' and l[:2][1][2] == "positive":
          d.append( f"{tweet} | there atleast is 1 neutral and 1 positive words in a sentence of {length} **{cat}**" )
        elif l[:2][0][2] == 'negative' and l[:2][1][2] == "neutral" or l[:2][0][2] == 'neutral' and l[:2][1][2] == "negative":
          d.append( f"{tweet} | there atleast is 1 neutral and 1 negative words in a sentence of {length} **{cat}**" )
        elif l[:2][0][2] == 'negative' and l[:2][1][2] == "positive" or l[:2][0][2] == 'positive' and l[:2][1][2] == "negative":
          d.append( f"{tweet} | there atleast is 1 positive and 1 negative words in a sentence of {length} **{cat}**" )
        if l[:2][0][2] == 'negative' and l[:2][1][2] == "negative":
          d.append( f"{tweet} | there atleast is 2 negative words in a sentence of {length} **{cat}**" )
        if l[:2][0][2] == 'positive' and l[:2][1][2] == "positive":
          d.append( f"{tweet} | there atleast is 2 positive words in a sentence of {length} **{cat}**" )
  return d

# add categeory to tweet, based on the word category.
def addCatTweet1( tweets, data ):
  d = []
  for tweet in tweets:
    if len( clean( tweet ) ) > 0: 
      freg = 0; cat = ''; l = []
      for key, item in data.items():
        if key in tweet and item[0] > freg:
          cat = item[1]
          l.append(( key, item[0], item[1] ))
      # tweet = clean( tweet )
      # length = len(tweet.split(' '))
      
      if len( l ) > 2:
        first = l[:2][0][2]; second = l[:2][1][2]
        # print( "here...", first,  second )
        if first == 'neutral' and second == "neutral":
          d.append( f"{tweet} | **{cat}**" )
        elif l[:2][0][2] == 'positive' and l[:2][1][2] == "neutral" or l[:2][0][2] == 'neutral' and l[:2][1][2] == "positive":
          d.append( f"{tweet} | **{cat}**" )
        elif l[:2][0][2] == 'negative' and l[:2][1][2] == "neutral" or l[:2][0][2] == 'neutral' and l[:2][1][2] == "negative":
          d.append( f"{tweet} | **{cat}**" )
        elif l[:2][0][2] == 'negative' and l[:2][1][2] == "positive" or l[:2][0][2] == 'positive' and l[:2][1][2] == "negative":
          d.append( f"{tweet} | **{cat}**" )
        if l[:2][0][2] == 'negative' and l[:2][1][2] == "negative":
          d.append( f"{tweet} | **{cat}**" )
        if l[:2][0][2] == 'positive' and l[:2][1][2] == "positive":
          d.append( f"{tweet} | **{cat}**" )
  return d

# put tweet in list by label
# return pos, neg, nuetral labels.
def seperateTweet( data ):
  pos = []
  neg = []
  neu = []
  for tweet in data:
    # tweetClean = clean1( tweet.lower() )
    # print( tweetClean )
    if re.search("neutral$", tweet ):
      neu.append( tweet )
    elif re.search("negative$", tweet ):
      neg.append( tweet )
    elif re.search("positive$", tweet ):
      pos.append( tweet )
  return [pos, neg, neu]
      
# write data to text file. receive array and write data line by line.
def writeData(filename, data):
  with open(filename, "w", encoding="utf-8") as obj:
    obj.writelines( data )
    

# write data to text file. receive array and write data line by line.
def writeData1(filename, data):
  data = [ f"{d[0]}, {d[1]}\n" for d in data ]
  with open(filename, "w", encoding="utf-8") as obj:
    obj.writelines( data )
    
# process negative data
def negProcess():
  d = {}
  data = read("negative.txt")
  data = clean( data )
  # process functions.
  data = removeStopWords( data )
  data = getFreq1( data )
  data = sortByValue( data )
  # data = filterMoreThanFreq( data )
  data = addCat1( data, "negative" )
  for item in data:
    d[ item[0] ] = [item[1], item[2]]
  return d
    
# process positive data
def posProcess():
  d = {}
  data = read("positive.txt")
  data = clean( data )
  # process functions.
  data = removeStopWords( data )
  data = getFreq1( data )
  data = sortByValue( data )
  # data = filterMoreThanFreq( data )
  data = addCat1( data, "positive" )
  for item in data:
    d[ item[0] ] = [item[1], item[2]]
  return d 

# process neutral data
def neuProcess():
  d = {}
  data = read("neutral.txt")
  data = clean( data )
  # process functions.
  data = removeStopWords( data )
  data = getFreq1( data )
  data = sortByValue( data )
  # data = filterMoreThanFreq( data )
  data = addCat1( data, "neutral" )
  for item in data:
    d[ item[0] ] = [item[1], item[2]]
  return d

# get all the words that are common in all data files.
# and keep the word with the most freguency.
def getCommon( neg, pos, neu ):
  common = {}
  for key, value in neg.items():
    if key in pos.keys() and key in neu.keys():
      if value[0] > pos[key][0] and value[0] > neu[key][0]:
        common[key] = [value[0], "negative" ]
      if pos[key][0] > value[0] and pos[key][0] > neu[key][0]:
        common[key] = [pos[key][0], "positive" ]
      if neu[key][0] > value[0] and neu[key][0] > pos[key][0]:
        common[key] = [ neu[key][0], "neutral" ]
  # add remaining left words.     
  for key, item in neu.items():
    if key not in common.keys():
      common[key] = item 
  # add remaining left words form postive.     
  for key, item in pos.items():
    if key not in common.keys():
      common[key] = item 
  # add remaining left words from negative .     
  for key, item in neg.items():
    if key not in common.keys():
      common[key] = item 
  return common

# turn dict into string.
def dictToStrList( data ):
  d = []
  for val in data:
    d.append( f"{val[0]}, {val[1][0]}, {val[1][1]}\n" )
  return d



# read data.
# data = read()
# data = getFreq( data )
# data = sortByValue( data )
# writeData1("word_freq.txt", data )
# 
tweets = readLines()#
seperate = seperateTweet( tweets )
# write data to files. 
writeData( "positive.txt", seperate[0] )
writeData( "negative.txt", seperate[1] )
writeData( "neutral.txt", seperate[2] )
# # 
negList = negProcess()
neuList = neuProcess()
posList = posProcess()
d = negList | neuList | posList
d = sortByValueArr( d )
d = dictToStrList( d )
writeData("word_freq.txt", d )
print("done writting word-freq to file.")
# 
# 
# data = getCommon( negList, posList, neuList )
# newTweets = addCatTweet1( tweets[ : 100 ], data )
# writeData("result.txt", newTweets )

print("done..")