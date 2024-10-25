def biggest(insert_integer: str, original_number: str) -> str:
    for i in range(len(original_number)):
        if int(original_number[i]) < int(insert_integer):
            return f'{original_number[:i]}{insert_integer}{original_number[i:]}'
        else:
            continue
    return f'{original_number}{insert_integer}'


if __name__ == '__main__':
    a, b = input().split()
    print(biggest(a, b))
