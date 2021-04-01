class Stack:
    def __init__(self):
        self.stack = [0] * 1000
        self.current = 0

    def empty(self):
        return self.current == 0

    def push(self, item):
        self.stack[self.current] = item
        self.current += 1

    def pop(self):
        self.current -= 1
        item = self.stack[self.current]
        return item


BRACKETS = {"(": ")", "[": "]", "<": ">"}

def checBracketSequance(seq: str):
    stack = Stack()
    for curr_br in seq:
        if curr_br in BRACKETS:
            stack.push(curr_br)
        else:
            if stack.empty():
                return False
            stack_br = stack.pop()
            if BRACKETS[stack_br] != curr_br:
                return False


    return stack.empty()



with open("input.txt") as f:
    n = int(f.readline())
    for test_num in range(n):
        test = f.readline().strip()
        if checBracketSequance(test):
            print("Yes")
        else:
            print("No")
