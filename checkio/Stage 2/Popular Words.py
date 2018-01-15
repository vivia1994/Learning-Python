from collections import Counter


def popular_words(text, words):
    # your code here
    dict = []
    dict1 =Counter(text.lower().replace("\n"," ").replace(","," ").replace("."," ").split(" "))

    print(dict1)

    del dict1['']
    dict=dict1.copy()
    for key in dict1.keys():
        if not key in words:
            del dict[key]
    for i in words:
        if not i in dict.keys():
            dict[i]=0
    print("dict",dict)
    return dict


if __name__ == '__main__':


    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
