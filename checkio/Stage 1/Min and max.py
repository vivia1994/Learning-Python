def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, key=None):
    return get_first_from_sorted(args, key, False)


def max(*args, key=None):
    return get_first_from_sorted(args, key, True)


# def min(*args, **kwargs):
#     key = kwargs.get("key", None)
#
#     sort_source = args if len(args) > 1 else args[0]
#     if isinstance(sort_source,set):
#         rel = sort_source.pop();
#     elif type(sort_source)==type(i for i in range(0,1)):
#         rel = sort_source.next()
#     else:
#         rel = sort_source[0]
#     if key !=None:
#         for each in sort_source:
#             if key(each) < key(rel):
#                 rel = each
#     else:
#         for each in sort_source:
#             if each < rel:
#                 rel=each
#     return rel
#
#
# def max(*args, **kwargs):
#     key = kwargs.get("key", None)
#     return None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
