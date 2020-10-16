# def Divide_without_remainder(number, n):
#     divisions = 0
#     for i in range(1, n + 1):
#         if number % i == 0:
#             divisions += 1
#     if divisions == n:
#         print('This number can be divided by each of the numbers from 1 to {}'.format(n))
#     else:
#         print("arg")
#
#
# Divide_without_remainder(2520, 10)


def Divide_without_remainder(maximum_divisor):
    Divisions = 0
    number_to_find = maximum_divisor
    found = False
    while not found:
        for i in range(1, maximum_divisor + 1):
            if number_to_find % i == 0:
                Divisions += 1
            if Divisions == maximum_divisor:
                print("the smallest number that can be divided by each of the numbers from 1 to {} is {}".format(maximum_divisor, number_to_find))
                found = True
        Divisions = 0
        number_to_find += 1


Divide_without_remainder(30)