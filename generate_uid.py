import random
import string
import sys

listOfUIDs = set()
keyValueDict = {}

def get_random_string():
    vowels = "AEIOU"
    consonants = "".join(set(string.ascii_uppercase) - set(vowels))
    firstChar = random.choice(consonants)
    return firstChar + ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(int(random.choice('345'))))

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

test = ['1', '2', '3', '4', '6', '1', '2', '3', '33', '27', '67', '10009', '10009']
for t in test:
    print("Test Integer:", t, "Value:", get_value(t))
# print(generate_random_id())
# print(keyValueMap)
