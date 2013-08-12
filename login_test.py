import urllib2;

def main():
	userMailUrl="http://tieba.baidu.com/f?kw=%BB%FD%CA%AF%CC%C3&frs=yqtb"
	req=urllib2.Request(userMailUrl)
	resp=urllib2.urlopen(req)
	respHtml=resp.read()
	print "respHtml",respHtml

main()