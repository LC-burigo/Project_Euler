def Sum_square_difference(number):
    Sum_of_the_numbers = 0
    Sum_of_the_squares = 0
    for i in range(1, number + 1):
        Sum_of_the_numbers += i
        Sum_of_the_squares += i * i

    Square_of_the_sum_of_the_numbers = Sum_of_the_numbers * Sum_of_the_numbers
    # print(Sum_of_the_numbers)
    # print(Square_of_the_sum_of_the_numbers)
    # print(Sum_of_the_squares)
    Difference = Square_of_the_sum_of_the_numbers - Sum_of_the_squares
    print(Difference)


Sum_square_difference(100)