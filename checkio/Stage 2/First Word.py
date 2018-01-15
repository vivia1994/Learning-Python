import re

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    print(iter(re.findall(r"\b(\w+((\'\w+)*))\b",text)).__next__()[0])
    # for i in iter(re.findall(r"(\w+((\'\w+)*))\s",text)).__next__():
    #     print("1----",i)
    return iter(re.findall(r"\b(\w+((\'\w+)*))\b",text)).__next__()[0]


if __name__ == '__main__':
    first_word("greetings, friends")
    first_word("don't touch it")
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
