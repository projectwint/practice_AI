#목표 상태 6의 위치를 파이썬 코드로 탐색
#단, 시작은 1부


#각 노드가 연결된 정보 표현
DFS_graph = {1: [2, 3],
             2: [1, 4, 5],
             3: [1, 6],
             4: [2],
             5: [2],
             6: [3]}

#초기 각 노드가 방문된 정보 표현(빈 리스트)
visited = []

def dfs(DFS_graph, start):
    visited.append(start)
    print(visited) #방문한 지점들을 출력하기

    for node in DFS_graph[start]:
        #만약 현재 지점이 방문한 적이 없다면 visted에 추가

        if node not in visited:
            dfs(DFS_graph, node) #함수 재호출

dfs(DFS_graph, 1)
