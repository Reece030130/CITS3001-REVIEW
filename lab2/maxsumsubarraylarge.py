
def max_subarray(xs: list[int] ,left ,mid ,right) -> int:
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += xs[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += xs[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def max_sum_subarray_divide_and_conquer(xs: list[int]) -> int:
    # if left == right:
    #     return xs[left]
    # mid = (left + right) // 2
    # left_sum = max_sum_subarray_divide_and_conquer(xs, left, mid)
    # right_sum = max_sum_subarray_divide_and_conquer(xs, mid + 1, right)
    # cross_sum = max_subarray(xs, left, mid, right)
    # return max(left_sum, right_sum, cross_sum)
    max_so_far = float('-inf')
    max_ending_here = 0
    for i in xs:
        max_ending_here += i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return 0 if max_so_far <= 0 else max_so_far


if __name__ == '__main__':
    num = int(input())
    arraylist = list(map(int, input().split()))
    print(max_sum_subarray_divide_and_conquer(arraylist))
