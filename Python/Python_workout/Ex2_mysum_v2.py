def mysum(*args):
    sum = 0 
    for i in args:
        sum += i
    return sum

print(mysum(1,2,3))

def wordSummary(words):
    wordSum = 0
    shortestWord = words[0]
    longestWord = ''
    for word in words:
        assert isinstance(word, str), "Argument should be a list of words"
        wordSum += len(word)
        if len(word) > len(longestWord):
            longestWord = word
        if len(word) < len(shortestWord):
            shortestWord = word
    print("Longest word is " + longestWord + ", shortest word is " + shortestWord + " and average word length is " + str(wordSum/len(words)))

wordSummary(['ball', 'architecture', 'piece', 'python', 'gun'])