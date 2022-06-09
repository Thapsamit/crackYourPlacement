class MyStack:

    def __init__(self):
        self.quIn = []
        self.quOt = []

    def push(self, x: int) -> None:
        while len(self.quIn)!=0:
            self.quOt.append(self.quIn.pop())
        self.quIn.append(x)
        while len(self.quOt)!=0:
            self.quIn.append(self.quOt.pop())
    def pop(self) -> int:
        return self.quIn.pop(0)
        
    def top(self) -> int:
        return self.quIn[0]
        
    def empty(self) -> bool:
        if len(self.quIn)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()