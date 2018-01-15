# def checkio(game_result):
#
#     for i in range(len(game_result)):
#         if all(row[i] == "X" for row in game_result):
#             return "X"
#         if all(row[i] == "O" for row in game_result):
#             return "O"
#
#         if game_result[i].count("X") == len(game_result):
#             return "X"
#         if game_result[i].count("O") == len(game_result):
#             return "O"
#
#     row_count_x = 0
#     row_count_o = 0
#     for i in range(len(game_result)):
#         if game_result[i][i] == "X":
#             row_count_x += 1
#         if game_result[i][i] == "O":
#             row_count_o += 1
#     if row_count_x == len(game_result):
#         return "X"
#     if row_count_o == len(game_result):
#         return "O"
#
#     row_count_x = 0
#     row_count_o = 0
#     for i in range(len(game_result)):
#         if game_result[i][len(game_result) - i - 1] == "X":
#             row_count_x += 1
#         if game_result[i][len(game_result) - i - 1] == "O":
#             row_count_o += 1
#     if row_count_x == len(game_result):
#         return "X"
#     if row_count_o == len(game_result):
#         return "O"
#     return "D"


def checkio(result):
    print(result)
    rows = result
    # print(zip(*rows))
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

if __name__ == '__main__':
    checkio(["X.O","XX.","XOO"])
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio([
    #     "X.O",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins"
    # assert checkio([
    #     "OO.",
    #     "XOX",
    #     "XOX"]) == "O", "Os wins"
    # assert checkio([
    #     "OOX",
    #     "XXO",
    #     "OXX"]) == "D", "Draw"
    # assert checkio([
    #     "O.X",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins again"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
