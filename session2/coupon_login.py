import urllib
import urllib2
import cookielib

cookiejar = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

opener.open("http://www.couponmom.com/")

data = urllib.urlencode({"email": "gfitch@gaf3.com", "password": "nainet"})

response = opener.open("http://www.couponmom.com/loginprocess.php", data)

print response.read()
print response.geturl()