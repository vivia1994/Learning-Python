def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    x=""
    for i in phrases:
        print(i)
        x = i.replace("right","left") if x=="" else x+","+i.replace("right","left")
    print(x)
    return x

if __name__ == '__main__':
    left_join(("left", "right", "left", "stop"))
    left_join(("bright aright", "ok"))
    left_join(("brightness wright",))
    left_join(("enough", "jokes"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
