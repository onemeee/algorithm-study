INF = int(1e9)

# 노드의 개수 및 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("INF", end='')
        else:
            print(graph[a][b], end='')
    print()
