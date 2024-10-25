def iguana():
    return None


if __name__ == '__main__':
    number = int(input())
    grid_of_characters = []
    for i in range(number):
        grid_of_characters.append(list(input().split()))
    print(number)
    for i in grid_of_characters:
        print(i)
