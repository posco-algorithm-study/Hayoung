while True:
    a = input()

    stack = []
    
    if a == '.':
        break

    for i in a:

        if (i == '(') or (i == '['):
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                print("no")
                break
            else:
                stack.pop()
            
        elif i == ']':
            if not stack or stack[-1] == '(':
                print("no")
                break
            else:
                stack.pop()
    else:
        if not stack:
            print("yes")
        else:
            print("no")

                
                    
                