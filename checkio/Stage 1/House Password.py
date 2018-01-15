# import re
# def checkio(data):
#
#     #replace this for solution
#     if len(data) < 10:
#         return False
#     if len(re.findall("\d+",data)) != 0 and len(re.findall("[a-z]+",data)) != 0 and len(re.findall("[A-Z]+",data)) != 0:
#         return True
#     return False


checkio = lambda s: not(len(s) < 10 or s.isdigit() or s.isalpha() or s.islower() or s.isupper())


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
