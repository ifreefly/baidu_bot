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
    foundH1user = re.search('<h1\s+class="(.*?)"\s+title="(.*?)"\s+>(.*?)<\/h1>', respHtml);
    print "foundH1user=",foundH1user;
    if(foundH1user):
        h1user = foundH1user.group("title");
        print "h1user=",h1user; 
###############################################################################
if __name__=="__main__":
    main();