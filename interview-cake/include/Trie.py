class Trie:
    def __init__(self):
        # print("In init function.")
        self.wordNum = 0
        self.prefixNum = 0
        self.edges = {}

    def addWord(self, word):
        # print(word)
        if word == '':
            self.wordNum += 1
        else:
            self.prefixNum += 1
            firstCharacter = word[0]
            restOfWord = word[1:]
            # print(firstCharacter)
            if firstCharacter not in self.edges:
                self.edges[firstCharacter] = Trie()
            self.edges[firstCharacter].addWord(restOfWord)

    def countWords(self, word):
        if word == '':
            return self.wordNum

        firstCharacter = word[0]
        restOfWord = word[1:]

        if firstCharacter not in self.edges:
            return 0
        else:
            return self.edges[firstCharacter].countWords(restOfWord)

    def countPrefixes(self, prefix):
        if prefix == '':
            return self.prefixNum

        firstCharacter = prefix[0]
        restOfPrefix = prefix[1:]
        # print("Searching for '%s' as a prefix"%(firstCharacter))

        if firstCharacter not in self.edges:
            return 0
        else:
            return self.edges[firstCharacter].countPrefixes(restOfPrefix)

    def getWords(self):
        pass

def main():
    print("Testing Code for Trie Class")

    print("Creating Trie object:")

    t = Trie()

    stringList = ['first','face','fire', 'faced', 'fir']
    # wordList = [list(s) for s in stringList]

    prefix = 'fi'

    for word in stringList:
        t.addWord(word)
        print("Prefix '%s' has %s words in the Trie."%(prefix, t.countPrefixes(prefix)))

    # for debugging
    # print(t.edges)
    # print(t.edges['f'].edges)
    # print(t.edges['f'].edges['i'].edges)

if __name__ == "__main__":
    main()
