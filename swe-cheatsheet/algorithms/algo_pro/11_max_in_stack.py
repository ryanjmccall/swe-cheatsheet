class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, v):
        self.stack.append(v)
        if self.max_stack:
            new_max = max(v, self.max_stack[-1])
        else:
            new_max = v

        self.max_stack.append(new_max)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def max(self):
        return self.max_stack[-1] if self.max_stack else None


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)

for _ in range(len(s.stack)):
    print(f'{s.max()} {s.pop()}')
