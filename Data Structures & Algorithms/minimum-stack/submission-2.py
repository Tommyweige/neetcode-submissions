class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [0]
        self.currentindex = 0
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        if val < self.stack[self.minstack[-1]]:
            self.minstack.append(self.currentindex)
        else:
            self.minstack.append(self.minstack[-1])
        self.currentindex += 1

    def pop(self) -> None:

        self.stack.pop()
        self.minstack.pop()
        self.currentindex -= 1


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minstack[-1]]
