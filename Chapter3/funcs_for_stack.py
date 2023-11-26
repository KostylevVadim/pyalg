from Chapter3.Stack import Stack

def reversestring(str: str):
    x = Stack()
    for elem in str:
        x.push(elem)
    y = ''
    while x.isEmpty() == False:
        y+=x.pop()
    return y


def is_good_skob(str):
    s = Stack()
    balanced = True
    index = 0
    while index < len(str) and balanced:
        symbol = str[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
    
def evaluate(str: str):
    
    if str:
        elems = str.split()
        stack=Stack()
        for elem in elems:
            # print(elem, '\n',stack)
            if elem.isdigit():
                stack.push(int(elem))
            elif elem in '+-*/':
                
                b = stack.pop()
                a = stack.pop()
                print(a, elem ,b)
                if elem == '+':
                    stack.push(a+b)
                if elem == '-':
                    stack.push(a-b)
                if elem == '*':
                    stack.push(a*b)
                if elem == '/':
                    stack.push(a/b)
        return stack.peek()

def func():
    pass