def count_primes_medium(x: int) -> int:
    primes = 0
    for i in range(2, x+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes += 1
    return primes


if __name__ == '__main__':
    print(count_primes_medium(int(input())))
