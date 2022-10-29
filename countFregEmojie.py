''' 
get freq of emojies.

outout file is: emojie.txt
'''
import json
import re
from emoji_translate.emoji_translate import Translator
from commonSubroutines import write


emo = Translator(exact_match_only=False, randomize=True)
FILENAME = "clean_tweets.txt"

# read data line-by-line
def readLines():
  data = ""
  with open( FILENAME, "r", encoding="utf8" ) as obj: 
    data = obj.readlines()
  return data

# read entire data
def read():
  data = ""
  with open( FILENAME, "r", encoding="utf-8" ) as obj: 
    data = obj.read()
  return data

# clean
def process( data ):
  data = data.lower()
  data = re.sub("[a-z0-9\s,.-|='!\":;+-]", "", data )
  data = " ".join( data.split() )
  return data 

# get frequency of imojies.
def freq( data ):
  d = {}
  for i in data:
    if i in d.keys(): d[i] += 1
    else: d[i] = 1
  return d

# assign meaning to imojie
def emoDef( data ):
  d = {}
  for k, v in data.items():
    m = emo.demojify(k)
    d[k] = [ v, m ]
  return d
    



data = read()
data = process( data )
# print( data )
data = freq( data )
# print( data )
data = emoDef( data )
print( f"Length of Imojies: {len(data.keys())}" )
data = str( data )
write("emojies.txt", data )
print("\ndone...........")