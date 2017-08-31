#!/usr/bin/python3

import json
from difflib import get_close_matches
import sys

data = json.load(open("data.json", "r"))

dataKeys = data.keys()


def getDef(w):

    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, dataKeys)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, dataKeys)[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, dataKeys)[0]]
        elif yn == "N" or yn == "n":
            return("Word not found.")
        else:
            return("We didn't understand your entry")
    else:
        return("Word not found.")

def printDef(output):
    if type(output) == list:
        print("Definition:")
        for item in output:
            print(item)
    else:
        print("Definiton:")
        print(output)


if len(sys.argv) > 1:
    word = sys.argv[1]
    defAnswer = getDef(word)
    printDef(defAnswer)
else:
    word = input("Type your word: ")
    defAnswer = getDef(word)
    printDef(defAnswer)