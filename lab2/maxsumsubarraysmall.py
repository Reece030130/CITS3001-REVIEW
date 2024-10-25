def max_sum_subarray_better(xs: list[int]) -> int:
    best = 0
    for lwr in range(len(xs)):
        total = 0
        for i in range(lwr, len(xs)):
            total += xs[i]
            best = max(best, total)
    return best


if __name__ == '__main__':
    num = int(input())
    arraylist = list(map(int, input().split()))
    print(max_sum_subarray_better(arraylist))


