from collections import defaultdict, deque


def flavoursgalore(flavours, relations):
    galore = defaultdict(list)
    in_degree = [0] * (flavours + 1)

    for x, y in relations:
        galore[y].append(x)
        in_degree[x] += 1

    queue = deque([i for i in range(1, flavours + 1) if in_degree[i] == 0])
    distance = [1] * (flavours + 1)
    processed_nodes = 0

    while queue:
        node = queue.popleft()
        processed_nodes += 1
        for neighbor in galore[node]:
            distance[neighbor] = max(distance[neighbor], distance[node] + 1)
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if processed_nodes != flavours:
        return -1
    return max(distance)


if __name__ == '__main__':
    flavours = int(input())
    relation = int(input())
    relations = [tuple(map(int, input().split())) for _ in range(relation)]
    result = flavoursgalore(flavours, relations)
    print(result)
