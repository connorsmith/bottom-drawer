from include import Stack

class MaxStack:
    def __init__(self):
        self.dataStack = Stack.Stack()
        self.maxStack = Stack.Stack()

    def insert(self, item):
        self.dataStack.insert(item)

        if self.maxStack.isEmpty() or item >= self.maxStack.peek():
            self.maxStack.insert(item)

    def pop(self):
        popVal = self.dataStack.pop()

        if popVal == self.maxStack.peek():
            self.maxStack.pop()

        return popVal

    def getMax(self):
        return self.maxStack.peek()

def main():
    m = MaxStack()
    m.insert(1)
    m.insert(3)
    m.insert(2)
    m.insert(4)

    print(m.getMax())
    for i in range(3):
        m.pop()
    print(m.getMax())

if __name__ == "__main__":
    main()