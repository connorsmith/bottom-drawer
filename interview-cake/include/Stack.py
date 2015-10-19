class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, newVal):
        self.data.append(newVal)
        self.size += 1

def main():
    s = Stack()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    print(s.pop())
    print(s.peek())

if __name__ == "__main__":
    main()