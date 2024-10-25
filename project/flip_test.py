from collections import deque, defaultdict


def flip(a, b, image):
    visited = set()
    cell_to_component = {}
    neighbors = {}
    for row in range(a):
        for col in range(b):
            if (row, col) not in visited:
                potential = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                stack = deque([(row, col)])
                neighbors.setdefault((row, col), set())
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        cell_to_component[current] = (row, col)
                        for x, y in potential:
                            new_row, new_col = current[0] + x, current[1] + y
                            if 0 <= new_row < a and 0 <= new_col < b:
                                if image[new_row][new_col] == image[row][col] and (new_row, new_col) not in visited:
                                    stack.append((new_row, new_col))
                                else:
                                    neighbor_comp = cell_to_component.get((new_row, new_col))
                                    if neighbor_comp and neighbor_comp != (row, col):
                                        neighbors.setdefault((row, col), set()).add(neighbor_comp)
                                        neighbors.setdefault(neighbor_comp, set()).add((row, col))
    print((find_farthest_and_largest_length(neighbors) + 1) // 2)


def dfs(node, adjacency_list, visited):
    visited.add(node)
    max_distance = 0
    farthest_node = node

    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dist, far_node = dfs(neighbor, adjacency_list, visited)
            if dist + 1 > max_distance:
                max_distance = dist + 1
                farthest_node = far_node

    return max_distance, farthest_node

# Function to find the farthest node and then calculate the largest length (diameter) from that node
def find_farthest_and_largest_length(adjacency_list):
    # Step 1: Perform DFS to find the farthest node from an arbitrary starting node
    start_node = next(iter(adjacency_list))
    visited = set()
    farthest_length, farthest_node = dfs(start_node, adjacency_list, visited)

    # Step 2: Perform DFS from the farthest node found to calculate the largest length (diameter)
    visited = set()  # Reset visited set
    largest_length, final_farthest_node = dfs(farthest_node, adjacency_list, visited)

    # Return both the farthest node and the largest length from it (the diameter)
    return  largest_length


if __name__ == '__main__':
    a, b = map(int, input().split())
    image = []
    for i in range(a):
        c = list(input())
        image.append(c)
    print(flip(a, b, image))
