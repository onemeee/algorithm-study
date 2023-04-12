import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


#노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 각 노드에 연결 되어 있는 노드에 대한 정보 리스트
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선에 대한 정보받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b 노드로 이동하는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 존재하는 동안

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
