__author__ = 'septiadi'


import requests,urllib2
from bs4 import BeautifulSoup


domain = raw_input("Enter DOMAIN to crawl: ")
#domain = 'blog.detik.com'
r = requests.get('http://'+domain+'/')


#r.text is raw data from given url
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.title)

ContentLenght = 0;

for link in soup.find_all('img'):
    src = link.get('src')

    try:
        if(src[0] == '/' and src[1] != '/'):
            src = 'http://'+domain+''+src
        elif(src[0] != '/' and src[0] != 'h'):
            src = 'http://'+domain+'/'+src
        elif(src[0] == '/' and src[1] == '/'):
            src = 'http:'+src
    except:
        pass

    print(src)

    #myurl = 'http://blog.detik.com/statics/images/front/ico_rss.jpg'


    try:
        response = urllib2.urlopen(src)
        header = response.info().headers

        for value in header:
            info = value.split(': ');
            if(info[0] == 'Content-Length'):
                ContentLenght += int(info[1]);
                print(' size: ' + info[1] + ' bytes' + ' the total become: ' + str(ContentLenght) + ' bytes')
            #break
    except:
        print(' failed to get image')


print('Final total ' + str(ContentLenght) + ' bytes')
