n, m = map(int, input().split())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(m)]