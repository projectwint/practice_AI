#너비 우선 탐색의 방법으로 목표 상태 6의 위치를 탐색
#단, 시작은 1부터

#queue는 FIFO(First-In-First-Out)구조를 갖고, 먼저 들어간 것부터 우선적으로 나간다.
#삽입이 이루어지는 것을 rear, 삭제가 이루어지는 것은 front


from collections import deque
#각 노드가 연결된 정보 표현

BFS_graph = {1: [2, 3],
             2: [1, 4, 5],
             3: [1, 6],
             4: [2],
             5: [2],
             6: [3]}

#초기 각 노드가 방문된 정보 표현
visited = []

def bfs(BFS_graph, start):
    queue = deque([start]) #queue를 이용

    while queue: #queue 리스트에 아무것도 없을 때까지 계속 반복
        node = queue.pop() #현재 방문하고 있는 지점(노드)

        #만약 현재 지점이 방문한 적이 없다면 visited에 추가
        if node not in visited:
            visited.append(node)
            print(visited) #방문한 경로 출력하기

            queue.extendleft(BFS_graph[node])

bfs(BFS_graph, 1)
