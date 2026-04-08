
class MyQueue:

    def __init__(self):
        self.lis = []
        self.lis1 = []
        

    def push(self, x: int) -> None:
        self.lis.append(x)
       
        

    def pop(self) -> int:
        self.peek()
        return self.lis1.pop()

        
        

    def peek(self) -> int:
        if not self.lis1:
            while self.lis:
                self.lis1.append(self.lis.pop())
        return self.lis1[-1]    

        
        

    def empty(self) -> bool:
        return not self.lis and not self.lis1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()