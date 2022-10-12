import json
import re
from commonSubroutines import write

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
  data = re.sub("[a-z0-9\s,.-|='!\":;]", "", data )
  data = " ".join( data.split() )
  return data 

# get frequency of imojies.
def freq( data ):
  d = {}
  for i in data:
    if i in d.keys(): d[i] += 1
    else: d[i] = 1
  return d



data = read()
data = process( data )
# print( data )
data = freq( data )
# print( data )
data = str( data )
write("emojies.txt", data )
print("\ndone...........")