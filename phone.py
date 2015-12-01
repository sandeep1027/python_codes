'''
This code is meant to filter only indian numbers. if you find any bug, logic error please reply back to me.
'''

import re
import urllib2
#read file
files=open("19-9-2015.txt",'r')
fh=files.read()
r = re.findall(r'(?:\+?\d{2}[ -]?)?\d{10}', fh)
visited=[]

#check the number on sever for validation 
def pars_html(numb,ori):
    if ori not in visited:
        url="http://trace.bharatiyamobile.com/?numb="+numb
        page=urllib2.urlopen(url)
        page_data=page.read()
        if "This is not a valid Indian Mobile Number." in page_data:
            print "No-->",numb
        else:
            files1 = open('phone_filter.txt','a')
            files1.write(numb)
            files1.write("\n")
            print "done-->",numb
            
    visited.append(ori)


def check_number(numb):
    rmtwo=""
    varlen=len(str(numb))
    mkstr=str(numb)
    rmtwo=mkstr[:3]
    if varlen>10 and rmtwo=="+91":
        str1=str(numb)
        rmtwo1=str1[3:]
        pars_html(rmtwo1,numb)
    else:
        if (rmtwo=="+92" or rmtwo=="+88" or rmtwo=="+86") and rmtwo!="+91" :
            print "not in-->",numb
        else:
           pars_html(numb,numb)
        '''
    if numb not in visited:
        url="http://trace.bharatiyamobile.com/?numb="+rmtwo
        page=urllib2.urlopen(url)
        page_data=page.read()
        if "This is not a valid Indian Mobile Number." in page_data:
            print "yes-->",numb,"-->",rmtwo
            visited.append(numb)
        else:
            files1 = open('phone_filter.txt','a')
            files1.write(rmtwo)
            files1.write("\n")
            print "done->",numb,"-->",rmtwo
            visited.append(numb)
     '''
for phone in r:
    check_number(phone)
