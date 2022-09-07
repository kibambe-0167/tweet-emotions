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

FILENAME = "clean_tweets.txt"
NEGATIVE = ['fuck','bolaya','jealous','shit','bad','unpleasant', 'worse','sucks','suck']
POSITIVE = ['love','like','best','better','lovely','amazing','great','greatest']
NATIVE_WORD_STOP = ['ga', 'se', 'mo', 'gore', 'jo', 'be','ke', 'ka', 're']

# get frequency of words
def getFreq( data ):
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
  # d = collections.OrderedDict( d )
  return d

# read data by
def read():
  data = ""
  with open( FILENAME, "r", encoding="utf8" ) as obj: 
    data = obj.read()
  data = ' '.join( data.split() )
  return data

# clean the data
def clean( data ):
  # exceot this chars.
  data = re.sub("[^\sa-z0-9]", "", data.lower() )
  data = ' '.join( data.split() )
  return data

# get words with freq >= 50
def filterMoreThanFreq( data ):
  d = []
  for item in data:
    if item[1] >= 40:
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

# read data.
tweets = readLines()# 
data = read()
# process functions.
data = clean( data )
data = removeStopWords( data )
data = getFreq( data )
data = sortByValue( data )
data = filterMoreThanFreq( data )
data = addCat( data ) # print( data )
data = addCatTweet( tweets, data )
for i in data[ : 50]:
  print( i ); print()