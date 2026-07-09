# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,value):
#         self.stack.append(value)
#     def pop(self,value):
#         self.stack.remove(value)
#     def peek (self,value):
#         self.stack
# s= Stack ()
# s.push(3)
# s.push(5)
# s.push(6)
# s.push('+')
# s.push('*')
# print(s.stack)
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    def is_empty(self):
        return len(self.stack) == 0
input_stack = Stack()
input_stack.push(3)
input_stack.push(5)
input_stack.push(6)
input_stack.push('+')
input_stack.push('*')
print("Original Input Stack:", input_stack.stack)
eval_stack = Stack()
for item in input_stack.stack:
    if isinstance(item, int):
        eval_stack.push(item)
    else:
        b = eval_stack.pop()
        a = eval_stack.pop()
        if item == '+':
            eval_stack.push(a + b)
        elif item == '*':
            eval_stack.push(a * b)
final_result = eval_stack.pop()
print("Final Evaluation Result:", final_result)

