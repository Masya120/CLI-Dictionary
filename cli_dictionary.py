#!/usr/bin/python3
import sys
import json
from difflib import get_close_matches


data = json.load(open("data.json", "r"))
dataKeys = data.keys()


def get_def(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return get_matches(word)

def get_matches(word):
    if len(get_close_matches(word, dataKeys)) > 0:
        user_response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, dataKeys)[0])
        if user_response == "Y" or user_response == "y":
            return data[get_close_matches(word, dataKeys)[0]]
        else:
            return "Sorry. Word not found."


def print_def(output):
    if type(output) == list:
        print("Definition:")
        for item in output:
            print(item)
    elif output == "Sorry. Word not found.":
        print(output)
    else:
        print("Definiton:")
        print(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        asked_word = sys.argv[1]
        def_answer = get_def(asked_word)
        print_def(def_answer)
    else:
        asked_word = input("Type your word: ")
        def_answer = get_def(asked_word)
        print_def(def_answer)