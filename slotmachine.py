#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand
import random

item1 = random.randint(0, 3)
item2 = random.randint(0, 3)
item3 = random.randint(0, 3)
item4 = random.randint(0, 3)
item5 = random.randint(0, 3)
item6 = random.randint(0, 3)

fruits = ['&#127815;',
          '&#127813;',
          '&#127827;',
          '&#127822;']

print(item1, ":", item2, ":", item3, ":", item4, ":", item5, ":", item6)

def slot_machine(item1, item2, item3, item4, item5, item6):
    if item1 == item2 and item2 == item3:
        return "100 gamestop giftcard"
    elif item1 == item2 or item2 == item3:
        return "Something midly intresting"
    else: 
        return "absolutley NOTHING"

reward = slot_machine(item1, item2, item3, item4, item5, item6)
print('You get', reward)
