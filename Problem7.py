def Position_of_a_prime(number):
    count = 0
    position = 0
    prime_number_to_find = 1
    while position < number:
        for n in range(1, prime_number_to_find + 1):
            if prime_number_to_find % n == 0:
                count += 1
        if count == 2:
            position += 1
        count = 0
        prime_number_to_find += 1

    print(prime_number_to_find - 1)


Position_of_a_prime(10001)

# fastest way
def n_th_prime(n):
    b = [2]
    while len(b) < n:
        for num in range(3, n * 11, 2):
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                b.append(num)

    print(list(sorted(b))[n - 1])


n_th_prime(10001)

