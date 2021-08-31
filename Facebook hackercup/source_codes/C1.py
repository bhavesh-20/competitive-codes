def dfs(graph, visited, c,i):
    visited[i] = True
    arr = []
    if i in graph:
        for j in graph[i]:
            if not visited[j]:
                x = dfs(graph, visited,c, j)
                arr.append(x)
    return_value = c[i-1]
    if len(arr)>0:
        if i == 1:
            arr.sort(reverse=True)
            m = arr[0]
            if len(arr) > 1:
                m += arr[1]
        else:
            m = max(arr)
        return_value += m
    return return_value

for _t in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    graph = {}
    for _ in range(n-1):
        node_1, node_2 = map(int,input().split())
        if node_1 not in graph:
            graph[node_1] = {node_2}
        else:
            graph[node_1].add(node_2)
        if node_2 not in graph:
            graph[node_2] = {node_1}
        else:
            graph[node_2].add(node_1)
    visited = [False] * (n+1)
    ans = dfs(graph, visited, c, 1)
    print(f"Case #{_t+1}: {ans}")
