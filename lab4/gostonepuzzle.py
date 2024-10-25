from collections import deque


def gostonepuzzle(s, t):
    if sorted(s) != sorted(t):
        return -1
    queue = deque([(s, 0)])
    visited = {s}
    while queue:
        current_state, moves = queue.popleft()
        moves += 1
        dot_index = current_state.find('..')
        for i in range(len(current_state) - 1):
            if i == dot_index or i == dot_index - 1:
                continue
            temp = list(current_state)
            temp[dot_index], temp[dot_index + 1] = temp[i], temp[i + 1]
            temp[i], temp[i + 1] = '.', '.'
            new_state = ''.join(temp)
            if new_state[:-2] == t[:-2]:
                return moves
            if new_state not in visited:
                queue.append((new_state, moves))
                visited.add(new_state)

    return -1


if __name__ == '__main__':
    length = int(input().strip())
    initial_stone = input().strip() + ".."
    target_stone = input().strip() + ".."
    print(gostonepuzzle(initial_stone, target_stone))
