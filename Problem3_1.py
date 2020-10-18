def prime_divisor(number):
    if number > 1:
        factors = []
        prime_list = []
        i = 2
        count = 0
        while i <= number:
            if number % i == 0:
                factors.append(i)
                for e in range(1, i + 1):
                    if i % e == 0:
                        count += 1
                if count == 2:
                    prime_list.append(i)

            count = 0
            i += 1
    else:
        print(number, "is not a prime number")

    print(factors)
    print(prime_list)
    print(max(prime_list))


prime_divisor(10)