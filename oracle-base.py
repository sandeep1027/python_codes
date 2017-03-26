import requests
from lxml.html import fromstring
from lxml import cssselect
from lxml import html
from Queue import Queue
from threading import Thread
import os

'''
  set the number of threads
  @type {Number}
 '''
num_fetch_threads = 30

'''
queue array
@type {[type]}
'''
queue_ = Queue()


'''
download url it would be like https://oracle-base.com/dba/{category}/{filename.{extension}}
@type {String}
'''
download_url = 'https://oracle-base.com/dba/'

'''
page url
@type {String}
'''
page_url = 'https://oracle-base.com/dba/scripts'

'''
tags category
@type {Array}
'''
catg_array = ['monitoring', '10g', '11g', '12c', 'constraints', 'miscellaneous', 'rac', 'resource_manager', 'script_creation', 'security', 'weblogic']

'''
script dir
'''
script_dir = os.path.dirname(os.path.abspath(__file__))

'''
folder name
'''
folder_name = "oracle-base"

'''
Destination dir
'''
dest_dir = os.path.join(script_dir, folder_name)

'''
function to fetch fata from url
@param url given input url
'''
def fetchData(url):
	data =requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
	return data

'''
 File write function.
 @param filename filename
 @param content text content
'''
def fileWrite(filename, content, category):
    path = os.path.join(dest_dir, category, filename)
    file_handler = open(path, 'w')
    file_handler.write(content.text)
    file_handler.close()

'''
 Main Thread function which handle most of the things
'''
def MainThread(i, q):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and only exit when
    the main thread ends.
    """
    while True:
        queue_ = q.get()
		#loop through till 60
        for i in range(1, 60):
        	xpath_ = ''
			#get the index
        	index = queue_[2]
        	for j in range(1, 3):
        		xpath_ = '//*[@id="content"]/div['+str(index)+']/div['+str(j)+']/ul/li['+str(i)+']/p/a/text()'
        		data = queue_[1].xpath(xpath_)
        		if data:
					print "Downloading "+data[0]+" file of category "+queue_[0]
					url = download_url+queue_[0]+'/'+data[0]
					con = fetchData(url)
					fileWrite(data[0], con, queue_[0])
        q.task_done()

# Set up some threads to fetch the content
for i in range(num_fetch_threads):
    worker = Thread(target=MainThread, args=(i, queue_,))
    worker.setDaemon(True)
    worker.start()

'''
 Main Function
'''
def main():
	index = 1;
	#extract the main html content
	page_content = fetchData(page_url)
	tree = html.fromstring(page_content.content)
	for catg in catg_array:
		index = index + 1
		path_ = os.path.join(dest_dir, catg)
		os.makedirs(path_)
		queue_.put((catg, tree, index))
	queue_.join()

if __name__ == '__main__':
    main()
