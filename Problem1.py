# def multiples_of_3_and_5(number):
#     List_numbers = []
#     Sum_numbers = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             List_numbers.append(i)
#             Sum_numbers += i
#
#     print(List_numbers)
#     print(Sum_numbers)
#
#
# multiples_of_3_and_5(1000)
########################################################################################################################
print(sum(i for i in range(21) if i % 3 == 0 or i % 5 == 0))
