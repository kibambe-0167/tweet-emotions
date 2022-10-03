import re


# read data by
def read( FILENAME="emoji_tweets_sentence_tweets_categorisation.txt" ):
  data = ""
  with open( FILENAME, "r", encoding="utf8" ) as obj: 
    data = obj.read()
  data = ' '.join( data.split() )
  return data

# read data by lines
def readLines( FILENAME ):
  data = ""
  with open( FILENAME, "r", encoding="utf8" ) as obj: 
    data = obj.readlines()
  return data

# write lines
def writeLines(filename, data):
  data = [ f"{d}\n" for d in data ]
  with open(filename, "w", encoding="utf-8") as obj:
    obj.writelines( data )
        

# clean the data without removing data
def cleanWithoutLabel( data ):
  # cleans a given sentence or phrase.
  # exceot this chars.
  data = ' '.join( [ a for a in [i for i in data.split(' ')] if not re.search("^http", a) ] )
  data = re.sub("[^\sa-z0-9]", "", data.lower() )
  data = ' '.join( data.split() )
  return data