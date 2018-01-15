def checkio(str_number, radix):
    result=0
    temp=0
    x=0
    for i in str_number:
        if i.isdigit():
            temp = int(i)
        if i.isalpha():
            temp=ord(i)-55
        if temp >= radix:
            return -1
        if x+1==len(str_number):
            result = result+temp
        else:
            result =result+ temp*pow(radix,len(str_number)-x-1)
        x+=1
    print("result",result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("AF", 16)
    checkio("101", 2)
    checkio("101", 5)
    checkio("Z", 36)
    checkio("AB", 10)

    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
