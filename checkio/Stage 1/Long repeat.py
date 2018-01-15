from collections import Counter
import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """

    maxstr = ""
    x = 0
    y = len(line) - 1
    for i in line:
        y = len(line)
        if x < len(line):
            for j in reversed(line):
                if y>=0:
                    subs = line[x:y]
                    dict = Counter(subs)
                    # print(x,y,subs,len(subs),maxstr,len(maxstr),len(dict.keys()))
                    if len(dict.keys())==1 and len(subs) > len(maxstr):
                        maxstr = subs
                        # print("maxstr__",maxstr)
                y -= 1
        x += 1
    # print("maxstr:",maxstr,len(maxstr))
    return len(maxstr)


if __name__ == '__main__':
    # long_repeat('sdsffffssse')
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
