# -*- coding: utf-8 -*-
'''#百度错误代码:
err_code:40  请输入验证码完成发帖
'''
import urllib,urllib2,cookielib,re;
import json;
def sign():
  sign_url='http://tieba.baidu.com/sign/add';
  find_like_tieba=[];
  succeed_sign_tieba=[];
  failed_sign_tieba=[];
  print '正在尝试签到';
  tbs=get_tbs();
  print '获取喜欢的贴吧ing...';
  like_tieba='http://tieba.baidu.com/f/like/mylike';
  resp=urllib2.urlopen(like_tieba).read();
  re_tieba_tr='<tr>(?P<tr>.*?)</tr>';
  re_like_tieba='<a href=".*?" title="(?P<like>.*?)">.*?</a>';
  find_like_tieba_tr=re.finditer(re_tieba_tr,resp);
  for item in find_like_tieba_tr:
    like=re.search(re_like_tieba,item.group());
    if(like!=None):
      find_like_tieba.append(like.group('like'));
  #print find_like_tieba;
  #print '我喜欢的贴吧:'
  for mylike_tieba in find_like_tieba:
    #构造签到数据头:
    #print unicode(mylike_tieba,'gbk');
    sign_request={'ie':'utf-8','kw':mylike_tieba,'tbs':tbs}
    sign_request=urllib.urlencode(sign_request);
    sign_request=urllib2.Request(sign_url,sign_request);
    sign_resp=urllib2.urlopen(sign_request);
    #print sign_resp;
    sign_resp=json.load(sign_resp);
    #print sign_resp;
    if sign_resp['error']=='' :
       user_sign_rank = int(sign_resp['data']['uinfo']['user_sign_rank']);                      #第几个签到
       cont_sign_num = int(sign_resp['data']['uinfo']['cont_sign_num']);                        #连续签到
       cout_total_sing_num = int(sign_resp['data']['uinfo']['cout_total_sing_num']);            #累计签到
       print "签到成功,第%d个签到,连续签到%d天,累计签到%d天" %(user_sign_rank, cont_sign_num, cout_total_sing_num);
       succeed_sign_tieba.append(mylike_tieba);
    elif sign_resp['error']==u'亲，你之前已经签过了':
      #print mylike_tieba;
      succeed_sign_tieba.append(mylike_tieba);
    else :#签到失败处理
      failed_sign_tieba.append(mylike_tieba);
  print 'succeed:'
  print_tieba(succeed_sign_tieba);
  print 'failed:';
  print print_tieba(failed_sign_tieba);

def print_tieba(tieba):
  for item in tieba:
    print unicode(item,'gbk');
    #print item.decode('unicode_escape');
  
def get_tbs():
  tbs_url='http://tieba.baidu.com/dc/common/tbs';
  tbs_resp=urllib2.urlopen(tbs_url).read();
  print tbs_resp;
  tbs=re.search('"tbs":"(?P<tbs>.*?)"',tbs_resp).group('tbs');
  print 'tbs:',tbs;
  return tbs;
      
def checkAllCookiesExist(cookieNameList, cookieJar) :
    cookiesDict = {};
    for eachCookieName in cookieNameList :
        cookiesDict[eachCookieName] = False;
     
    allCookieFound = True;
    for cookie in cookieJar :
        if(cookie.name in cookiesDict) :
            cookiesDict[cookie.name] = True;
     
    for eachCookie in cookiesDict.keys() :
        if(not cookiesDict[eachCookie]) :
            allCookieFound = False;
            break;
 
    return allCookieFound;
    
def baidu(username,password):#尝试登录百度
  test_url='http://yun.baidu.com';
  login_path='https://passport.baidu.com/v2/api/?login';
  try:
    cookie=cookielib.CookieJar();
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie));
    urllib2.install_opener(opener);
    opener.addheaders=[('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31')];
    #获取cookie
    baiduMainUrl = "http://www.baidu.com/";
    resp = urllib2.urlopen(baiduMainUrl);
    #获取奇葩的token
    print "to get token value";
    getapiUrl = "https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true";
    getapiResp = urllib2.urlopen(getapiUrl);
    #print "getapiResp=",getapiResp;
    getapiRespHtml = getapiResp.read();
    foundTokenVal = re.search("bdPass\.api\.params\.login_token='(?P<tokenVal>\w+)';", getapiRespHtml);
    if(foundTokenVal):
        tokenVal = foundTokenVal.group("tokenVal");
        print "tokenVal=",tokenVal;
    else:
      print 'foundTokenVal is null';
      
    post_dic={
	'staticpage':'http://www.baidu.com/cache/user/html/v3Jump.html',
	'charset':'UTF-8',
	'token':tokenVal,
	'tpl':'mn',
	'apiver':'v3',
	#'tt':,
	#'codestring':,
	'isPhone':'false',
	'safeflg':0,
	'u':'http://www.baidu.com/',
	'quick_user':0,
	#'usernamelogin':1,
	'splogin':'rate',
	'username':username,
	'password':password,
	#'verifycode':'',
	'mem_pass':'on',
	#'ppui_logintime':14791
	'callback':'parent.bd__pcbs__c5crjq',
      };
    postdata=urllib.urlencode(post_dic);
    req=urllib2.Request(login_path,postdata);
    resp=urllib2.urlopen(req)
    #data=urllib2.urlopen(test_url).read();
    cookiesToCheck = ['BDUSS', 'PTOKEN', 'STOKEN', 'SAVEUSERID'];
    loginBaiduOK = checkAllCookiesExist(cookiesToCheck, cookie);
    if(loginBaiduOK):
       print "+++ Emulate login baidu is OK, ^_^";
       #return 'ok'
       print 'ok'
    else:
       print "--- Failed to emulate login baidu !"
       #return 'failed';
       print 'failed';
    sign();
    print '尝试结束，看疗效...';
    #return data;
  except Exception,e:
    print str(e);
    
#我喜欢的贴吧
#http://tieba.baidu.com/f/like/mylike?
#re:<a href="\/f\?kw=.*?" title=".*">.*?<\/a>
user='youremail';
password='yourpassword';
baidu(user,password);