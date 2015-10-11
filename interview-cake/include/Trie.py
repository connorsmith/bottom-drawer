class Trie:
    def __init__(self):
        # print("In init function.")
        self.wordNum = 0
        self.prefixNum = 0
        self.edges = {}

    def addWord(self, word):
        # print(word)
        if word == []:
            self.wordNum += 1
        else:
            self.prefixNum += 1
            firstCharacter = word.pop(0)
            # print(firstCharacter)
            if firstCharacter not in self.edges:
                self.edges[firstCharacter] = Trie()
            self.edges[firstCharacter].addWord(word)

    def countWords(self, word):
        if word == []:
            return self.wordNum

        firstCharacter = word.pop(0)

        if firstCharacter not in self.edges:
            return 0
        else:
            return self.edges[firstCharacter].countWords(word)

    def countPrefixes(self, prefix):
        if prefix == []:
            return self.prefixNum

        firstCharacter = prefix.pop(0)
        print("Searching for '%s' as a prefix"%(firstCharacter))

        if firstCharacter not in self.edges:
            return 0
        else:
            return self.edges[firstCharacter].countPrefixes(prefix)

def main():
    print("Testing Code for Trie Class")

    print("Creating Trie object:")

    t = Trie()

    stringList = ['first','face','fire', 'faced']
    wordList = [list(s) for s in stringList]

    for word in wordList:
        t.addWord(word)
        print(t.countWords(['f','i','r','e']))

    # print(t.edges)
    # print(t.edges['f'].edges)
    # print(t.edges['f'].edges['i'].edges)

if __name__ == "__main__":
    main()
