# перевертыш

ops = {'+': 2, '-': 2, '/': 1, '*': 1, '^': 0}

INPUT = '3 + 4 * 2 / (11 - 5)^2'

stack, OUTPUT, digit = [], [], False

for s in INPUT:

    if s in '0123456789':
        if len(OUTPUT) == 0:
            OUTPUT = [s] + OUTPUT
        else:
            if OUTPUT[0][-1] in '0123456789' and digit:
                OUTPUT[0] += s
            else:
                OUTPUT = [s] + OUTPUT
        digit = True
    else:
        digit = False

    if s == '(':
        stack = [s] + stack

    if s == ')':
        while stack != [] and stack[0] != '(':
            OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
        if stack != [] and stack[0] == '(':
            stack = stack[1:]
    if s in ops:
        while stack != [] and stack[0] in ops and ops[s] >= ops[stack[0]]:
            OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
        stack = [s] + stack

while stack != []:
    OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]

print('инфиксная запись:\t%s' % (INPUT))
print('постфиксная запись:\t%s' % (" ".join(reversed(OUTPUT))))
