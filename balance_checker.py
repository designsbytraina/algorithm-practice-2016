def parChecker(symbols):
    my_stack = Stack()
    balanced = True
    count = 0

    while count < len(symbols) and balanced:
        symbol = symbols[count]
        if symbol in "{[(":
            my_stack.push(symbol)
        else:
            if my_stack.isEmpty():
                balanced = False
            else:
                top = my_stack.pop()
                if not matches(top, symbol):
                    balanced = False

        count += 1

    if balanced and my_stack.isEmpty():
        return balanced

    else:
        balanced = False

    return balanced


def matches(open, close):
    openers = "{[("
    closers = ")]}"
    return openers.index(open) == closers.index(close)



