for TC in range(1, int(input())+1):
    stack = input().split()
    print(f'Case #{TC}:', end=' ')
    for _ in range(len(stack)):
        print(stack.pop(), end=' ')