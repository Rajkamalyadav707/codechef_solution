def priority(op):
    if op == '(':
        return 0;
    elif op == '+' or op == '-':
        return 1;
    elif op == '*' or op == '/' or op == '%':
        return 2;
    elif op == '^':
        return 3;

t = int(input());
for x in range(0, t):
    expr = str(input());

    stack = [];

    for i in range(0, len(expr)):
        if expr[i].isalpha():
            print(expr[i], end='');
        elif expr[i] == '(':
            stack.append(expr[i]);
        elif expr[i] == ')':
            ele = stack.pop();
            while ele != '(':
                print(ele, end='');
                ele = stack.pop();
        else:

            # now it must be an operand
            while len(stack) and priority(expr[i]) <= priority(stack[len(stack)-1]):
                ele = stack.pop();
                print(ele, end='');
            stack.append(expr[i]);

    while len(stack):
        ele = stack.pop();
        print(ele, end='');


    print("");
