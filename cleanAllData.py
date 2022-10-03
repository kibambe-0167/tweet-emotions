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

# import sub routines from common sub routing file
from commonSubroutines import read, readLines, cleanWithoutLabel, writeLines


def getLabel( data ):
    l = data.rindex(',')
    return [ data[ : l ], data[ l : ] ]

# read the entire data
data = readLines( "emoji_tweets_sentence_tweets_categorisation.txt" )




# use list comprehension to clean the lines.
data = [ f"{ cleanWithoutLabel( getLabel(line)[0] ) }, { cleanWithoutLabel( getLabel(line)[1] )}"  for line in data[ 1: ] ]

# 
# for line in data[ : 10]: print( line )


# t = "@Saboshego6 Eeh Moruti waka,  o suitile maan.  👌🏾. Letšatši le lebotse ,positive"
# print( getLabel(t) )
# 
# write data to file.
writeLines( "allTweetsClean.txt", data )

# 
print("\ndone..")