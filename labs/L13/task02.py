# [(2341234]
#  t
# ([)]

stack = [0] * 150
top = 0

# def init():
#     global top
#     top = 0
#
# def push(el):
#     global top
#     stack[top] = el
#     top += 1
#
# def empty():
#     return top == 0
#
# def pop():
#     global top
#     if empty():
#         return None
#     top -= 1
#     res = stack[top]
#     return res

class Stack:

    def __init__(self):
        self.elems = [0] * 1001
        self.top = 0

    def push(self, elem):
        self.elems[self.top] = elem
        self.top += 1

    def pop(self):
        # if self.empty():  # міститься у операції back()
        #     raise RuntimeError("Stack is empty")

        top_elem = self.back()
        self.top -= 1

        return top_elem

    def back(self):
        if self.empty():
            raise RuntimeError("Stack is empty")
        return self.elems[self.top - 1]

    def empty(self):
        return self.size() == 0

    def size(self):
        return self.top

    def clear(self):
        self.top = 0


# def check(par_seq):
#     stack = Stack()
#     for c in par_seq:
#         if c == "(" or c == "[":
#             stack.push(c)
#         else:
#             if stack.empty():
#                 return False
#             from_stack = stack.pop()
#             if c == ")" and from_stack != "(":
#                 return False
#             if c == "]" and from_stack != "[":
#                 return False
#
#     return stack.empty()

BRACKETS_OPEN =  ["(", "["]
def check(seq: str):
    stack = Stack()
    for curr_br in seq:
        if curr_br in BRACKETS_OPEN:
            stack.push(curr_br)
        else:
            if stack.empty():
                return False
            stack_br = stack.pop()
            if curr_br == "]" and stack_br != "[":
                return False
            elif curr_br == ")" and stack_br != "(":
                return False

    return stack.empty()




if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        for line in f:
            seq = line.strip()
            if check(seq):
                print("Yes")
            else:
                print("No")
