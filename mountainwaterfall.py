def mountainwaterfall(mountain: list, row: int, column: int):
    flowed = []
    stack_pos = []
    def flowing():
        while stack_pos:
            water_row, water_col = stack_pos.pop()
            if (water_row+1, water_col+0) not in flowed and mountain[water_row+1][water_col+0] != 'o':
                flowed.append((water_row+1, water_col+0))
                stack_pos.append((water_row+1, water_col+0))
                mountain[water_row+1][water_col+0] = '*'
                break
            else:
                if ((water_row+0, water_col+1) not in flowed and (water_row+0, water_col-1) not in flowed and mountain[water_row][water_col+1] != 'o' or
                        mountain[water_row][water_col-1] != 'o'):
                    flowed.append((water_row+0, water_col+1))
                    stack_pos.append((water_row+0, water_col+1))
                    mountain[water_row][water_col+1] = '*'
                    flowed.append((water_row+0, water_col-1))
                    stack_pos.append((water_row+0, water_col-1))
                    mountain[water_row][water_col-1] = '*'
                break
    for i in range(row):
        for j in range(column):
            if mountain[i][j] == '*' and mountain[i][j] not in flowed:
                stack_pos.append((i,j))
                flowing()

    return mountain

if __name__ == '__main__':
    row, column = map(int, input().split())
    len = row
    mountain = []
    while len:
        mountain.append(list(input()))
        len -= 1
    for i in mountainwaterfall(mountain, row, column):
        print(*i, sep='')