for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    q += [0] * m
    front = -1
    rear = n-1
    for _ in range(m):
        front += 1
        rear += 1
        q[rear] = q[front]
    front += 1
    print(f'#{tc} {q[front]}')