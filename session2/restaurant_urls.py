import re
import couponmon
    
if not couponmon.login("gfitch@gaf3.com","navinet"):
    exit("Login failed")

response = couponmon.opener.open("http://www.couponmom.com/restaurant-coupons-159")

links = re.findall('<a.*href="(free-.*?)".*?>',response.read())

for link in links:
    print link
