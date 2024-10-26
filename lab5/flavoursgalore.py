def flavoursgalore(galore :dict):
    return -1






if __name__ == '__main__':
    flavours = int(input())
    relationship = int(input())
    galore = {int(key): int(value) for _ in range(relationship) for key, value in [input().split()]}
    print(flavoursgalore(galore))
