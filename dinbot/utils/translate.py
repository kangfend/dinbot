#!/usr/bin/env python

import urllib2

def translate(kalimat, dari="auto", ke="auto"):
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	elemen = 'class="t0">'
	link = "http://translate.google.com/m?q=%s&sl=%s&hl=%s" % (kalimat.replace(" ", "+"), dari, ke)
	request = urllib2.Request(link, headers=agents)
	respon = urllib2.urlopen(request).read()
	hasil = respon[respon.find(elemen)+len(elemen):]
	hasil = hasil.split("<")[0]
	return hasil

if __name__ == '__main__':
	kalimat = 'Apa kabar?'
	print("%s >> %s" % (kalimat, translate(kalimat, 'id', 'en')))

