# import re
# def count_words(text, words):
#     count_result = 0
#     for word in words:
#         if len(re.findall(word,text.lower())) != 0:
#             count_result += 1
#     return count_result


def count_words(text, words):
    for w in words:
        print(w)
    return sum(w in text.lower() for w in words)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
