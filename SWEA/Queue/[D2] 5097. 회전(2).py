for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    front = 0
    for _ in range(m):
        front += 1
    front = front % n
    print(f'#{tc} {q[front]}')