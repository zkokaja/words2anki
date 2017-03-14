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

with open(filename) as f:
    for word in f.read().splitlines():
        definitions = wordApi.getDefinitions(word, limit=1)

        if definitions != None:
            print "%s\t%s" % (word, definitions[0].text.encode('utf-8'))
        else:
            print "No definition found: ", word

