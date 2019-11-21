import requests
import sys

score = 100
url = sys.argv[1]
print('request made to .....'+ url +'...' )
test= 0


try:
 response = requests.get(url)
 test = 1
except requests.exceptions.RequestException as e:
 print("Check your input ")

if test == 1:
 try:
    demo = response.headers['x-xss-protection']
    print("---XSS protection Looks fine---")  
 except KeyError:
   print("----xss protection header is not there---- ")
   score = score - 20

 try:
    demo = response.headers['X-Frame-Options']
    print("---clickjacking test passed---")  
 except KeyError:
   print("Looks like vulnerble to clickjacking ")
   score = score - 20

   
    try:
    demo = response.headers['content-security-policy']
    print("---CSP passed---")  
 except KeyError:
   print("Looks like dont have Content security policy header ")
   score = score - 5
   
   
       try:
    demo = response.headers['Access-Control-Allow-Origin']
    if demo == '*':
      print("---Misconfig in CORS headers---")
      score = score-5
    else:
      print("passed in CORS test")
 except KeyError:
   print("Looks like dont have CORS header | good to use it! ")
   score = score - 5



 print("###your score for headers analysis is " + str(score))

