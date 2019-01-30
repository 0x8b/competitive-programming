t = int(input())

m = {'}': '{', ']': '[', ')': '('}

for _ in range(t):
    s = list(input())

    stack = []

    c = True

    for b in s:
        if b in '[{(':
            stack.append(b)
        else:
            if len(stack) and stack[-1] == m[b]:
                stack.pop()
            else:
                c = False
                break
        
    print('YES' if c and len(stack) == 0 else 'NO')
