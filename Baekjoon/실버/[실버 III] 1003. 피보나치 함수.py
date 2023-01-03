for _ in range(int(input())):
    num_zero = [1, 0]
    num_one = [0, 1]
    target = int(input())
    for i in range(2, target+1):
        num_zero.append(num_zero[i-2] + num_zero[i-1])
        num_one.append(num_one[i-2] + num_one[i-1])
    print(num_zero[target], num_one[target])