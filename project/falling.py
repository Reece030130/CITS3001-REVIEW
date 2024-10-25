def falling(dominoes, relationships_list):
    graph = {}
    chaos_factors = []
    for start, goal in relationships_list:
        if start not in graph:
            graph[start] = []
        graph[start].append(goal)
    for i in range(1, dominoes + 1):
        chaos_factors.append(dfs(graph, i))
    return chaos_factors


def dfs(graph, start):
    stack = [start]
    visited = set()
    count = 0
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            count += 1
            if current in graph.keys():
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    return count


if __name__ == '__main__':
    dominoes, relationships = map(int, input().split())
    relationships_list = []
    for i in range(relationships):
        relationships_list.append(list(map(int, input().split())))
    print(*falling(dominoes, relationships_list))
