# [(2341234]
#  t
# ([)]

stack = [''] * 128
top = 0

def init():
    global top
    top = 0

def push(el):
    global top
    stack[top] = el
    top += 1

def empty():
    return top == 0

def pop():
    global top
    if empty():
        return None
    top -= 1
    res = stack[top]
    return res

dict_par = {']': "[", ")": "("}
def check(par_seq):
    init()
    # stack: (
    for c in par_seq:
        if c not in dict_par:
            push(c)
        else:
            closed_par = c # )
            cor_open_par = dict_par[closed_par]  # (
            if empty():
                return False
            from_stack = pop()  # (
            if cor_open_par != from_stack:
                return False
    return empty()



    while not empty():
        el = pop()
        print(el)
    return True


if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        for line in f:
            seq = line.strip()
            if check(seq):
                print("Yes")
            else:
                print("No")