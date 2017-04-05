#!/usr/bin/env python

import os
import sys

from wordnik import *

# Prints tab separated data to standard out. First column is the front of the
# card, while the second the next is the back; the word then its definition
# respectively.

try:  
    apiKey = os.environ["WORDNIK_API_KEY"]
except KeyError: 
    print "Please set the environment variable 'WORDNIK_API_KEY'"
    sys.exit(1)

if len(sys.argv) < 2:
    print "Expecting a file name containing words to find definitions for"
    sys.exit(1)

filename = sys.argv[1]
apiUrl   = 'http://api.wordnik.com/v4'
client   = swagger.ApiClient(apiKey, apiUrl)
wordApi  = WordApi.WordApi(client)

def getUsage(frequency):
    if   frequency < 10:  return "Rare"
    elif frequency < 50:  return "Low"
    elif frequency < 200: return "Medium"
    elif frequency < 400: return "High"
    elif frequency < 800: return "Very High"
    else:                 return "Common"

with open(filename) as f:
    for word in f.read().splitlines():
        definitions = wordApi.getDefinitions(word, limit=1)

        if definitions != None:

            definition = definitions[0].text.encode('utf-8')
            frequency = wordApi.getWordFrequency(word)

            if frequency != None:
                usage = getUsage(frequency.totalCount)
            else:
                usage = "Unknown"

            print "%s\t%s\t%s" % (word, definition, usage)
        else:
            print "No definition found: ", word

