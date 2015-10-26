from include import Stack

# O(n) time, O(k) space - depends on the number of parentheses
class ParenthesisMatcher:
    def __init__(self):
        self.parenStack = Stack.Stack()
        self.indexStack = Stack.Stack()

    def getMatchingParenthesisIndex(self, sentence, index):
        # returns None if no match exists
        for idx, character in enumerate(sentence):
            if character == '(':
                self.parenStack.insert(character)
                self.indexStack.insert(idx)
            elif character == ')':
                self.parenStack.pop()
                matchIndex = self.indexStack.pop()
                if matchIndex == None:
                    return None
                elif matchIndex == index:
                    return idx
        return None

def getMatchingParenthesisIndex(sentence, index):
    # deal with empty sentence case
    if sentence == "":
        return None

    # check to make sure the index is valid (assume it is for now)
    parenCount = 1
    matchIndex = index + 1

    for character in sentence[index+1:]:
        if character == "(":
            parenCount += 1
        elif character == ")":
            parenCount -= 1

        if parenCount == 0:
            return matchIndex
        else:
            matchIndex += 1

    return None

def main():
    '''
    Error handling cases: 
        - index doesn't correspond to a starting parenthesis 
        - there is no closing parenthesis for the one selected
        - parentheses don't match
        - string is empty

    '''

    # [testString, testIndex, desiredOutput]
    testCaseList = []
    testCaseList.append(["Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.",10,79])
    testCaseList.append(["(()", 0, None]) # unmatched paren 1
    testCaseList.append(["((())", 1, 4]) # unmatched paren 1
    testCaseList.append(["Tricked you(?)", 0, None]) # index doesn't correspond to a parenthesis
    testCaseList.append(["", 0, None]) # empty string


    p = ParenthesisMatcher()
    print("Using ParenthesisMatcher Class:")
    for caseNumber, testCase in enumerate(testCaseList):
        # print testCase
        print("Test Case %s passed: %s"%(caseNumber+1, p.getMatchingParenthesisIndex(testCase[0], testCase[1])==testCase[2]))

    print("\nUsing constant space getMatchingParenthesisIndex Function:")
    for caseNumber, testCase in enumerate(testCaseList):
        # print testCase
        print("Test Case %s passed: %s"%(caseNumber+1, getMatchingParenthesisIndex(testCase[0], testCase[1])==testCase[2]))    

if __name__ == "__main__":
    main()