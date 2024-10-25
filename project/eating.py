def eating(colour: list) -> int:
    color_list = {}
    for i in colour:
        if i in color_list:
            color_list[i] += 1
        else:
            color_list[i] = 1
    return len([key for key, value in color_list.items() if value == 1 or value % 2 != 0])


if __name__ == '__main__':
    count = input()
    colour = input().split()
    print(eating(colour))
