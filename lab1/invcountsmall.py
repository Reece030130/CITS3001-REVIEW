def insertion_sort(xs: list):
    counts = 0
    # Iterate through prefix lengths
    for l in range(1, len(xs)):
        # Insert xs[l] into sorted prefix xs[0:l]
        for i in range(l, 0, -1):
            # xs[i] is element being inserted
            if xs[i] < xs[i - 1]:
                # Wrong way around, swap them
                # Hint, this is an inversion!
                xs[i - 1], xs[i] = xs[i], xs[i - 1]
                counts += 1
            else:
                # xs[i] is in the right spot
                break
        # xs[0:l+1] is now sorted
    return counts


if __name__ == '__main__':
    num = int(input())
    list1 = list(map(int, input().split()))
    print(insertion_sort(list1))
