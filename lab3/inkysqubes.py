import math


def inky_squbes(L, R):
    # result = [int(R ** 0.5) - int(L**0.5)+1, int(round(R**(1/3))) - int(round(L**(1/3)))+1,
    #           int(R**(1/6)) - int(L**(1/6))+1]
    square_count = 0
    cube_count = 0
    sqube_count = 0
    #Such a nice mathod!
    y = math.ceil(L ** 0.5)
    for i in range(y, R + 1):
        if y * y <= R:
            square_count += 1
            y += 1
        else:
            break

    y = math.ceil(L ** (1/3))
    for i in range(y, R + 1):
        if y * y * y <= R:
            cube_count += 1
            y += 1
        else:
            break

    y = math.ceil(L ** (1/6))
    for i in range(y, R + 1):
        if y ** 6 <= R:
            sqube_count += 1
            y += 1
        else:
            break
    return f"{square_count} {cube_count} {sqube_count}"


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(inky_squbes(a, b))
