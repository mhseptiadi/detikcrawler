__author__ = 'septiadi'


import requests,urllib2
from bs4 import BeautifulSoup

def imageParsing():

    domain = raw_input("Enter DOMAIN to crawl: ")
    r = requests.get('http://'+domain+'/')

    soup = BeautifulSoup(r.text, 'html.parser')

    ContentLenght = 0;
    images = soup.find_all('img')
    for image in images:
        src = image.get('src')

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

    print("\n")
    print('Total images counted ' + str(len(images)))
    print('Final total all image size ' + str(ContentLenght) + ' bytes')

imageParsing()
