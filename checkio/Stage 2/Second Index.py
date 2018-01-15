import re


def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    # pattern = re.compile(str)
    # print(re.findall(symbol,text).count(symbol))
    if re.findall(symbol, text).count(symbol) < 2:
        return None
    p = 0
    is_result = False
    for i in text:
        print(i,p)
        if is_result and i == symbol:
            print(p)
            return p
        if i == symbol:
            is_result = True
        p += 1



if __name__ == '__main__':
    # second_index("sims", "s")
    second_index("find the river", "e")
    # print('Example:')
    # print(second_index("sims", "s"))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert second_index("sims", "s") == 3, "First"
    # assert second_index("find the river", "e") == 12, "Second"
    # assert second_index("hi", " ") is None, "Third"
    # assert second_index("hi mayor", " ") is None, "Fourth"
    # assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    # print('You are awesome! All tests are done! Go Check it!')
