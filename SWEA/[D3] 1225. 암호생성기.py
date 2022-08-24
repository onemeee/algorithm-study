for tc in range(1, 11):
    n = input()
    nums = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
            num = nums.pop(0) - i
            if num <= 0:
                nums.append(0)
                break
            else:
                nums.append(num)
        if nums[-1] == 0:
            break
    result = ' '.join(map(str, nums))
    print(f'#{tc} {result}')