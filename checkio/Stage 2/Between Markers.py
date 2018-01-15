def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    print(text.find(begin), text.find(end))
    if (text.find(end) < text.find(begin) and text.find(end)!=-1 and text.find(begin)!=-1)or text.find(end) == 0:
        print("1--------")
        return ''
    elif text.find(end) == -1 and text.find(begin) == -1:
        print("2--------")
        return text
    elif text.find(end) == -1:
        print("3--------",text.split(begin)[0])
        return text.split(begin)[1]
    elif text.find(begin) == -1:
        print("4--------",text.split(end)[0])
        return text.split(end)[0]
    print("5--------")
    print(text.split(begin)[1].split(end)[0])
    return text.split(begin)[1].split(end)[0]


if __name__ == '__main__':
    between_markers('No [b]hi', '[b]', '[/b]')

    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
