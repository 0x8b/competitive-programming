N = int(input())

stack = [0]

instr = list(map(int, input().split()))

for i in range(N):
    cmd = instr[0]

    top = stack[-1]

    if cmd == 1:
        elem_to_push = instr[1]

        if elem_to_push < top:
            elem_to_push = top

        stack.append(elem_to_push)
    elif cmd == 2:
        stack.pop()
    elif cmd == 3:
        print(top)
