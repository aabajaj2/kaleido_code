import random
import string
import sys

listOfUIDs = set()
keyValueDict = {}

def get_random_string():
    firstChar = ''.join('')
    return ''.join(random.choice(string.ascii_uppercase+ string.digits) for i in range(int(random.choice('456'))))

def get_value(key):
    if key in keyValueDict:
        return keyValueDict.get(key)
    else:
        value = get_random_string()
        if value not in listOfUIDs:
            keyValueDict[key] = value
        else:
            newvalue = generate_random_id()
            keyValueDict[key] = newvalue
    return value

test = ['1', '2', '3', '4', '6', '1', '2', '3', '33', '27']
for t in test:
    print("Key:", t, "Value:", get_value(t))
# print(generate_random_id())

# print(keyValueMap)
