def gostonepuzzle(initial_stone: list, target_stone: list):

    return initial_stone, target_stone




if __name__ == '__main__':
    length = input()
    initial_stone = list(input())
    target_stone = list(input())
    print(gostonepuzzle(initial_stone, target_stone))