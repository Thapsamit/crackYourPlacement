class MyQueue:

    def __init__(self):
        self.stInput = []
        self.stOutput = []
        

    def push(self, x: int) -> None:
        while self.stInput:
            self.stOutput.append(self.stInput.pop())
        self.stInput.append(x)
        while self.stOutput:
            self.stInput.append(self.stOutput.pop())
        
    def pop(self) -> int:
        return self.stInput.pop()
        

    def peek(self) -> int:
        return self.stInput[-1]
    

    def empty(self) -> bool:
        if len(self.stInput)==0 and len(self.stOutput)==0:
            return True
        else:
            return False
   
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()