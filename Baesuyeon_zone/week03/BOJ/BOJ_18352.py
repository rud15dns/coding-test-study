import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #초기에는 모든 거리를 무한으로 설정
 
#노드의 개수, 간선의 개수, 최단거리 조건, 시작 노드를 입력받기
n, m, k, x = map(int, input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

#최단 거리 테이블을 무한으로 초기화
distance = [INF]*(n+1)
 
#모든 간선 정보를 입력받기
for _ in range(m):
    a,b = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,1)) #해당 문제에서는 비용이 1로 고정되어있으므로 c=1
 
def dijkstra(x):
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, x))
    distance[x] = 0
    #q가 비어있지 않다면
    while q:
        #가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        #현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드 확인
        for next_node, cost in graph[now]:
            new_dist = dist + cost
            #현재 노드를 거치면 이동 거리가 더 짧은 경우
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))
 
#다익스트라 알고리즘 실행
dijkstra(x)
 
#결과출력
result = []
#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    #도달할 수 없는 경우, 무한 출력
    if distance[i]==k:
        result.append(i)
if result : 
    for city in sorted(result):
        print(city)
else:
    print(-1)