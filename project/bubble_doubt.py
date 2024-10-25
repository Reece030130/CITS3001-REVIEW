


def bubble(bubbles: list, buckets: int) -> int:
    bucket_list = [[] * buckets]
    bubbles.sort()
    bubbles = np.array_split(bubbles, buckets)
    final = 0
    for bubble in bubbles:
        max_value = max(bubble)
        min_value = min(bubble)
        a = (max_value - min_value) ** 2
        final = final + a
    print(bubbles)
    b = [5]
    print(max(b), min(b))
    return final


if __name__ == '__main__':
    bubble_num, bucket_num = map(int, input().split())
    bubble_li = []
    for i in range(bubble_num):
        bubble_li.append(int(input()))
    print(bubble(bubble_li, bucket_num))
