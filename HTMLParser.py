from urllib import request
from html.parser import HTMLParser
import re

meeting_record=[]

class MyHTMLParser(HTMLParser):

    _curtag = ''
    _curattrs = None

    def handle_starttag(self, tag, attrs):
        self._curtag=tag
        self._curattrs=attrs

        if tag == 'time':
            if len(attrs) > 0:
                if tag == 'time' and 'datetime' in attrs[0]:
                    # print("attrs[0][1]__",attrs[0][1])
                    meeting_record[-1]['event_time'] = attrs[0][1]      # 最后一个元素
    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        tag=self._curtag
        attrs=self._curattrs

        if tag == 'a' or tag == 'span':
            if len(attrs) > 0:
                if 'href' in attrs[0]:
                    url = attrs[0][1]
                    if re.match(r'^/events/python-events/\d+/$', url):
                        meeting_record.append({'event_title': '', 'event_time': '', 'event_location': ''})
                        meeting_record[-1]['event_title'] += data
                elif 'event-location' in attrs[0]:
                    meeting_record[-1]['event_location'] += data
        self._curtag = ''
        self._curattrs= None

    def handle_comment(self, data):
        pass
    def handle_entityref(self, name):
        pass
    def handle_charref(self, name):
        pass

parser = MyHTMLParser()

with request.urlopen("https://www.python.org/events/python-events/") as req:
    data = req.read()
    with open(r"C:\Users\vlei002\Desktop\2.txt","wb") as file:
        file.write(data)
    parser=parser.feed(data.decode("utf-8"))
    print(meeting_record)