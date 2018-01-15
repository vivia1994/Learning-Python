from collections import Counter
def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    dict = Counter(data)
    print(dict,max(dict.keys(), key=lambda k: dict[k]))
    return max(dict.keys(), key=lambda k: dict[k])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
