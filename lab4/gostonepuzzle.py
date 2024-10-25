from collections import deque

def gostonepuzzle(s, t):
    queue = deque([(s, 0)])
    visited = set(s)
    while queue:
        current_state, moves = queue.popleft()
        if current_state == t:
            return moves
        empty_positions = []
        for i in range(len(current_state)):
            if current_state[i] == '.':
                empty_positions.append(i)
        for i in range(len(current_state) - 1):
            if current_state[i] != '.' and current_state[i + 1] != '.':
                new_state = current_state.copy()
                stones = [new_state[i], new_state[i + 1]]
                new_state[i] = '.'
                new_state[i + 1] = '.'
                new_state[empty_positions[0]] = stones[0]
                new_state[empty_positions[1]] = stones[1]
                if new_state == t:
                    return moves + 1
                state_tuple = tuple(new_state)
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    queue.append((new_state, moves + 1))

    return -1


if __name__ == '__main__':
    length = int(input().strip())
    initial_stone = list(input().strip())+['.'] * 2
    target_stone = list(input().strip())+['.'] * 2
    print(gostonepuzzle(initial_stone, target_stone))
