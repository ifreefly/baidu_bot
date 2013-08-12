# -*- coding: utf-8 -*-
#---------------------------------import---------------------------------------
import urllib2;
import re;
#------------------------------------------------------------------------------

def main():
    userMainUrl = "http://tieba.baidu.com/p/2525590943";
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html
    #<h1 class="h1user">crifan</h1>
    foundH1user = re.search(r'<h1.*?>(.*?)</h1>', respHtml);
    print "foundH1user=",foundH1user;
    if(foundH1user):
        h1user = foundH1user.group(1);
        print "文章标题:",h1user; 
###############################################################################
if __name__=="__main__":
    main();