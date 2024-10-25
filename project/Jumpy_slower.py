import itertools


def jumpy(time_limited: float, distance_children: list, children_speed: list) -> int:
    min_caught = children
    for perm in itertools.permutations(children_speed):
        caught = len([(i/j) for i, j in zip(distance_children, perm) if (i/j) > time_limited])
        if caught < min_caught:
            min_caught = caught
        if min_caught == 0:
            break
    return min_caught


if __name__ == '__main__':
    children, distance_wolf, speed = map(int, input().split())
    distance_children = list(map(int, input().split()))
    children_speed = list(map(int, input().split()))
    time_limited = distance_wolf / speed
    print(jumpy(time_limited, distance_children, children_speed))
