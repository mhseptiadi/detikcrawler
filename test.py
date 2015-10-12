import urllib2

ContentLenght = 0

src = 'http://secure-sg.imrworldwide.com/cgi-bin/m?ci=ind-detik&cg=0&cc=1&ts=noscript'

response = urllib2.urlopen(src)
header = response.info().headers

for value in header:
    info = value.split(': ');
    if(info[0] == 'Content-Length'):
        ContentLenght += int(info[1]);
        print(src + ' size: ' + info[1] + ' bytes' + ' the total become: ' + str(ContentLenght) + ' bytes')
        #break