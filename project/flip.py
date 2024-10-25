from collections import deque


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
    return (farther_node(neighbors) + 1) // 2


def farther_node(adjacency_list):
    largest_length = 0
    start_node = next(iter(adjacency_list))
    visited = set()
    max_distance, farthest_node = dfs(start_node, adjacency_list, visited)
    visited = set()
    max_distance, _ = dfs(farthest_node, adjacency_list, visited)
    largest_length = max(largest_length, max_distance)

    return largest_length


def dfs(node, adjacency_list, visited):
    visited.add(node)
    farthest_node = node
    max_distance = 0

    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dist, far_node = dfs(neighbor, adjacency_list, visited)
            if dist + 1 > max_distance:
                max_distance = dist + 1
                farthest_node = far_node

    return max_distance, farthest_node


# def flipped(original_dict, components):
#     collapse_count = 0
#
#     def sum_key_values(key):
#         return components[key] + sum(components[value] for value in original_dict[key])
#
#     while len(original_dict) > 1:
#         sorted_keys = sorted(original_dict, key=lambda k: (sum_key_values(k)), reverse=True)
#         current_key = sorted_keys[0]
#         value_to_add = set()
#         value_to_remove = original_dict[current_key]
#         for value in original_dict[current_key]:
#             if value in original_dict and value != current_key:
#                 for values in original_dict[value]:
#                     if values != current_key:
#                         value_to_add.add(values)
#                 original_dict.pop(value)
#         original_dict[current_key] = value_to_add
#         for key in list(original_dict.keys()):
#             if key != current_key:
#                 updated_values = set()
#                 for v in original_dict[key]:
#                     if v in value_to_remove:
#                         updated_values.add(current_key)
#                     else:
#                         updated_values.add(v)
#                 original_dict[key] = updated_values
#         collapse_count += 1
#         if len(original_dict) == 1:
#             break
#
#     return collapse_count


if __name__ == '__main__':
    a, b = map(int, input().split())
    image = []
    for i in range(a):
        c = list(input())
        image.append(c)
    print(flip(a, b, image))
