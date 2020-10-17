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


