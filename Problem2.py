def Fibonacci(limit_number):
    a = 1
    b = 2
    number_list = [a, b]
    Sum_even_numbers = 0
    while b < limit_number:
        a, b = b, a + b
        number_list.append(a)
        number_list.append(b)

    number_list = list(dict.fromkeys(number_list))
    number_list.pop()

    for number in number_list:
        if number % 2 == 0:
            Sum_even_numbers += number

    print(number_list)
    print(Sum_even_numbers)


Fibonacci(100000)