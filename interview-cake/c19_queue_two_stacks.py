from include import Stack

class TwoStacksQueue:
    def __init__(self):
        self.stackA = Stack.Stack()
        self.stackB = Stack.Stack()

    def enqueue(self, item):
        self.stackA.insert(item)
        # print("Insertion successful.")

    def dequeue(self):
        if self.stackB.isEmpty():
            # print("stackB is empty.")
            if self.stackA.isEmpty():
                # print("stackA is empty too.")
                return None
            else:
                while not self.stackA.isEmpty():
                    self.stackB.insert(self.stackA.pop())
        
        # stackB is not empty, pop the top item from the Stack
        return self.stackB.pop()


def main():
    q = TwoStacksQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())

if __name__ == "__main__":
    main()