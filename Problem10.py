def Sum_of_primes(number):
    list_of_primes = []
    if number > 1:
        count = 0
        i = 2
        while i <= number:
            for e in range(1, i + 1):
                if i % e == 0:
                    count += 1
            if count == 2:
                list_of_primes.append(i)
            count = 0
            i += 1

        print(sum(list_of_primes))
    else:
        print("The input number should be greater than 1")


Sum_of_primes(1000000)