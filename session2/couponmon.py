import urllib
import urllib2
import cookielib

opener = None

def login(email,password):

    import couponmon

    cookiejar = cookielib.CookieJar()

    couponmon.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

    couponmon.opener.open("http://www.couponmom.com/")

    data = urllib.urlencode({"email": email, "password": password})

    response = opener.open("http://www.couponmom.com/loginprocess.php", data)

    return 'error' not in response.geturl()