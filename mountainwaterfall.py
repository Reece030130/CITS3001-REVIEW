def mountainwaterfall(mountain: list, row: int, column: int):
    stack_pos = []
    for i in range(row):
        for j in range(column):
            if mountain[i][j] == '*':
                stack_pos.append((i,j))
                while stack_pos:
                    water_row, water_col = stack_pos.pop()
                    if mountain[water_row+1][water_col] != '*':
                        if mountain[water_row + 1][
                            water_col + 0] == '.' and 0 <= water_col+1 <= column and 0 <= water_row+0 <= row:
                            stack_pos.append((water_row + 1, water_col + 0))
                            mountain[water_row + 1][water_col + 0] = '*'
                        else:
                            for r_move, c_move in [(0, -1), (0, 1)]:
                                new_row = water_row + r_move
                                new_col = water_col + c_move
                                if 0 <= new_col < column and mountain[new_row][new_col] == '.':
                                    stack_pos.append((new_row, new_col))
                                    mountain[new_row][new_col] = '*'

    return mountain

if __name__ == '__main__':
    row, column = map(int, input().split())
    mountain = [list(input()) for _ in range(row)]
    result = mountainwaterfall(mountain, row, column)
    for i in result:
        print(*i, sep='')