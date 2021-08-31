def bfs(graph, visited, d, start_node):
    queue = [[start_node, 0]]
    d[start_node] = {}
    while len(queue) != 0:
        x = queue.pop(0)
        visited[x[0]] = True
        d[start_node][x[0]] = x[1]
        if x[0] in graph:
            for i in graph[x[0]]:
                if not visited[i]:
                    visited[i] = True
                    queue.append([i,x[1]+1])


for _t in range(int(input())):
    s = input()
    k = int(input())
    graph = {}
    for _ in range(k):
        str = input()
        if str[0] in graph:
            graph[str[0]].add(str[1])
        else:
            graph[str[0]] = {str[1]}
    d = {}
    for i in graph:
        visited = {chr(i): False for i in range(65,91)}
        bfs(graph, visited, d, i)
    count_array = {}
    for i in s:
        if i in count_array:
            count_array[i] += 1
        else:
            count_array[i] = 1
    minimum = 10**18
    alphabets = [chr(i) for i in range(65,91)]
    for i in alphabets:
        seconds = 0
        for j in count_array:
            if i!=j:
                if j in d and i in d[j]:
                    seconds += (d[j][i]) * count_array[j]
                else:
                    seconds = None
                    break
        if seconds != None:
            minimum = min(minimum, seconds)
    if minimum == 10**18:
        ans = "-1"
    else:
        ans = f"{minimum}"
    print(f"Case #{_t+1}: {ans}")
