import re
import time
import webbrowser

def match_with_url(data):
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
	if urls:
		time.sleep(2)
		webbrowser.open(urls[0])