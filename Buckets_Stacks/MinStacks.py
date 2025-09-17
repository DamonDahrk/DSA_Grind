class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
        #creating two stacks to compute

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

        #Here only o1 needed cuz we are updating minstack by comparing with last value appended
        #checking for if minstack is non empty else return the value only

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
