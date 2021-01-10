# def Max_Four_Horizontal_Grid():
#     Grid = [
#         [1, 2, 3, 4],
#         [2, 3, 4, 5],
#         [4, 6, 3, 6],
#         [9, 1, 3, 4]
#             ]
#
#     Product_Of_Four_Adjacent_Numbers = 0
#     The_Greatest = 0
#     for r in range(0, 4):
#         for c in range(0, 2):
#             Product_Of_Four_Adjacent_Numbers = Grid[r][c] * Grid[r][c + 1] * Grid[r][c + 2]
#             if Product_Of_Four_Adjacent_Numbers > The_Greatest:
#                 The_Greatest = Product_Of_Four_Adjacent_Numbers
#
#     print(The_Greatest)
#
#
# def Max_Four_Vertical_Grid():
#     Grid = [
#         [1, 2, 3, 4],
#         [2, 3, 4, 5],
#         [4, 6, 3, 6],
#         [9, 1, 3, 4]
#             ]
#
#     Product_Of_Four_Adjacent_Numbers = 0
#     The_Greatest = 0
#     for c in range(0, 4):
#         for r in range(0, 2):
#             Product_Of_Four_Adjacent_Numbers = Grid[r][c] * Grid[r + 1][c] * Grid[r + 2][c]
#             if Product_Of_Four_Adjacent_Numbers > The_Greatest:
#                 The_Greatest = Product_Of_Four_Adjacent_Numbers
#
#     print(The_Greatest)
#
#
# def Max_Four_Diagonal_Grid():
#     Grid = [
#         [1, 2, 3, 4],
#         [2, 3, 4, 5],
#         [4, 6, 3, 6],
#         [9, 1, 3, 4]
#             ]
#
#     row = 0
#     column = 0


