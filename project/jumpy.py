def jumpy(distance_wolf: int, speed: int, distance_children: list, children_speed: list, children: int) -> int:
    capture = children
    children_speed.sort()
    distance_children.sort()
    j = 0
    k = 0
    while k < children and j < children:
        if (distance_children[j] * speed + distance_wolf - 1) // distance_wolf <= children_speed[k]:
            capture -= 1
            j += 1
            k += 1
        else:
            k += 1
    return capture


if __name__ == '__main__':
    children, distance_wolf, speed = map(int, input().split())
    distance_children = list(map(int, input().split()))
    children_speed = list(map(int, input().split()))
    time_limited = distance_wolf / speed
    print(jumpy(distance_wolf, speed, distance_children, children_speed, children))
