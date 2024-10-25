def lost(row_sum: list, col_sum: list, matrix: list, number: int) -> list:
    for i in range(number):
        for j in range(number):
            value = min(col_sum[i], row_sum[j])
            matrix[j][i] = value
            row_sum[j] -= value
            col_sum[i] -= value
    return matrix if sum(row_sum) + sum(col_sum) == 0 else [[-1]]


if __name__ == '__main__':
    number = int(input())
    row_sum = list(map(int, input().split()))
    col_sum = list(map(int, input().split()))
    matrix = [[0] * number for _ in range(number)]
    for row in lost(row_sum, col_sum, matrix, number):
        print(*row)
