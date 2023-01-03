for i in range(int(input())):
    count = 0
    targets = input()
    factor = 0
    if targets:
        for target in targets:
            if target == '[':
                count += 1
            elif target == ']':
                count -=1
            if count > factor:
                factor = count
    print(2**(factor))