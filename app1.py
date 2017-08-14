import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

word = input("Type your word: ")


def getDef(w):

    w = w.lower()
    if w in data:
        return data[w]
    else:
        return("Word not found. Did you mean to type this word? " + get_close_matches(w, data.keys(), n=3, cutoff=0.8)[0])


print(getDef(word))