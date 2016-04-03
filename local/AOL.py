import random

import AOL_Keys as AOL

#this can take up to two arguments:
#chance is the chance of success
#mod is the "out of"; the default is two, meaning there are two
#possibilities.
#if no parameters are provided, then it's a 1/2 (50%) chance of
#returning true.
def _myRand(chance=1, mod=2):
    return random.randint(0,20)%mod < chance

#this returns a random index in the given range
def _randIndex(end):
    return random.randint(0, end-1)

#this returns a random replacement from the translation table
def _randResult(key):
    if type(AOL.words[key]) == type([]):
        end = len(AOL.words[key])
        return AOL.words[key][_randIndex(end)]
    else:
        return AOL.words[key]


def aol(text):
    words = text.lstrip().split(' ')

    returnString = ""
    newWord = ""

    if words[0] == "@ignore":
        returnString = ' '.join(words[1:])
    else:
        for word in words:
            newWord = word
            #90% chance of translating each word
            if _myRand(9,10):
                if (word.lower() in AOL.words):
                    newWord = _randResult(word.lower())
                else:
                    for substitution in AOL.subs:
                        #50% chance of substituting letters around, if the
                        #substitution is in the word
                        if substitution in newWord and _myRand():
                            newWord = newWord.replace(substitution, AOL.subs[substitution])
                #50% chance of raising the case
                if _myRand():
                    newWord = newWord.upper()
            returnString += newWord + " "

        #swap some letters around
        buildString = ""
        for i in range(0, len(returnString)-1, 2):
            if _myRand(1,6):
                buildString += returnString[i+1] + returnString[i]
            else:
                buildString += returnString[i] + returnString[i+1]

        #add some random acronyms to the end
        for i in range(_randIndex(10)):
            if _myRand(3,4):
                length = len(AOL.addons)
                buildString += AOL.addons[_randIndex(length)] + " "

        for i in range(_randIndex(20)):
            if _myRand(3,4):
                if _myRand(4,5):
                    buildString += "!"
                else:
                    buildString += "1"

        returnString = ""
        for i in buildString.split():
            #do some capitalization
            if _myRand():
                returnString += i.upper() + " "
            else:
                returnString += i.lower() + " "

    return returnString
