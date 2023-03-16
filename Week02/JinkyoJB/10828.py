import sys

stacks = []
    
a = int(sys.stdin.readline())

for i in range(a):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stacks.append(command[1])
    elif command[0] == 'pop':
        if len(stacks)==0:
            print(-1)
        else:
            print(stacks.pop())
    elif command[0]=='size':
        print(len(stacks))
    elif command[0]=='empty':
        if len(stacks)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stacks)==0:
            print(-1)
        else:
            print(stacks[-1])
            

