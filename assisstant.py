#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand

import random

message = random.randint(0, 5)
def assistant(Message):
    if Message == 0:
        return("Hi" ":" "Hello friend")
    elif Message == 1:
        return("Hi" ":" "What is it")
    elif Message == 2:
        return("Hello" ":" "HI :]")
    elif Message == 3:
        return("What's Up?" ":" "Not Much!")
    else:
        return("How are you?" ":" "I'm doing good thanks for asking!")
      

reply = assistant(message)
print(reply)


