import urllib
import re
import urlparse

#example url
url="http://www.mapsofindia.com/hotels-india/westbengal/kolkata.html"
visited=[]

def extract_email(url):
	page=urllib.urlopen(url)
	page_data=page.read()
	pat = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
	li = pat.findall(page_data)
	page.close()
	cleanlist = []
	[cleanlist.append(x) for x in li if x not in cleanlist]
	files = open('emails.txt','a')
	for show in cleanlist:
		#print show
		files.write(show)
		files.write("\n")
		print("done url ",url)
extract_email(url)
link_re = re.compile(r'href="(.*?)"')
dt=urllib.urlopen(url)
req=dt.read()
links=link_re.findall(req)
for link in links:
	link_new=urlparse.urljoin(url, link)
	res=bool('javascript' in link_new)
	if not res:
		res1=bool('css' in link_new)
		if not res1:
			if link_new not in visited:
				extract_email(link_new)
				visited.append(link_new)
