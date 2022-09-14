from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        return self.stack1.popleft()
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()