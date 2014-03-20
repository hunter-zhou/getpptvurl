#coding:utf-8
import time
import datetime
import urllib
import xmltodict
import json
import pptvkey


def getplaylist(url):
	s = urllib.urlopen(url).read()	
	pos = s.find('{"id":')
	pos1 = s.find(',',pos)
	
	id = s[pos+6:pos1]
	url = 'http://web-play.pptv.com/webplay3-0-%s.xml' % id
	s = urllib.urlopen(url).read()
	    
	j = xmltodict.parse(s);


	sforkey = j['root']['dt']['st']

	key = pptvkey.getplaykey(sforkey)
	
	ip =  j['root']['dt']['sh']
        
	rid =   j['root']['channel']['@rid']        
	        
	c = len( j['root']['dragdata']['sgm'])
                
	ret = []
	for i in range(0,c):
		url = 'http://%s/%s/%s?key=%s' %(ip,i,rid,key)
		ret.append( url)
	
	return ret

if __name__ == '__main__':

	r = getplaylist('http://v.pptv.com/show/zibl9ib2PJOXfaWMA.html')
	for i in r:
		print i

