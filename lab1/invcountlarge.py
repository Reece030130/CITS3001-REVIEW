# def merge_quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return merge_quick_sort(left) + middle + merge_quick_sort(right)

def merge_and_count(left, right):
    sorted_array = []
    i = j = inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            inversions += i

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array, inversions


def merge_sort_and_count_inversions(arr1):
    if len(arr1) <= 1:
        return arr1, 0

    mid = len(arr1) // 2
    left, left_inversions = merge_sort_and_count_inversions(arr1[:mid])
    right, right_inversions = merge_sort_and_count_inversions(arr1[mid:])
    merged, split_inversions = merge_and_count(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions
    return total_inversions


if __name__ == '__main__':
    num = int(input())
    list1 = list(map(int, input().split()))
    print(merge_sort_and_count_inversions(list1))
