import random

def readFile(filename):
    """ reads the given file and returns a list of strings in that file. """
    filehandle = open(filename, "r")
    contents = filehandle.read()
    stringList = contents.split()
    filehandle.close()
    return stringList

def starters(words, k):
    """ Takes alist of words and a parameter k and returns a list of
        tuples, each with the first k words of a sentence in the words
        list. """
    lst = []
    lst += [tuple(words[:k])]
    sentenceEnd = False
    for x in range(len(words)):
        end = words[x][-1]
        if sentenceEnd == True:
            lst += [tuple(words[x:x+k])]
            sentenceEnd = False
        if end in [".", "!", "?"]:
            sentenceEnd = True

    return lst


def learn(words, k):
    """ Takes the list of strings and a parameter k>=1 as input and
        returns a dictionary in which the keys are all the k-tuples
        of consecutive words in the dictionary and the value associated
        with a key is the list of all words - with repetitions - that 
        appear immediately after that k-tuple. """
    wordDict = {}
    for x in range(len(words)):
        key = tuple(words[x:x+k])
        if key in wordDict:
            wordDict[key] += words[x+k:x+1+k]
        else:
            wordDict[key] = words[x+k:x+1+k]

    return wordDict

def generate(markovD, length, starterList):
    """ Takes a Markov dictionary, the desired length of the output
        text, and list of the starter tuples  and generates random 
        text of the specified length or more. """
    randTup = random.choice(starterList)
    for word in randTup:
        print(word, end=' ')
    for x in range(length):
        word = random.choice(markovD[randTup])
        print(word, end=' ')
        tempLst = []
        for x in range(1, len(randTup)):
            tempLst += [randTup[x]]
        tempLst += [word]

        randTup = tuple(tempLst)
        if word[-1] in [".", "!", "?"]:
            randTup = random.choice(starterList)

    print()

def main():
    fileName = input("Enter the name of a training file: ")
    k = int(input("Enter k: "))
    n = int(input("Enter approximate output length: "))
    text = readFile(fileName)
    starts = starters(text, k)
    D = learn(text, k)
    generate(D, n, starts)



