import requests
r = requests.get('https://www.python.org')
r2 = requests.get('https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP')
print(r)
print(r.links)
print(r.text)
print(r.status_code)


"""
for api need to use beautifulsoup

from bs4 import BeautifulSoup 



"""




"""
# HTTP request codes 
https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP




Informational responses (100 – 199)
Successful responses (200 – 299)
200 -> ok
201 -> created
202 -> accepted 
203 -> Non-Authoritative information
204 -> No Content




Redirection messages (300 – 399)
Client error responses (400 – 499)
404 -> Not Found 
405 -> Method Not Allowed
406 -> Not acceptable 
407 -> Proxy authentication required
408 -> request Timeout
415 -> unsupported Media Type
423 -> Locked (webDav)
426 -> upgrade required
429 -> Too many requests 



 

Server error responses (500 – 599)
502 ->Bad Gateway
503 ->Service Unavailable
504 ->Gateway Timeout
505 ->HTTP Version Not Supported
507 ->Insufficient Storage (WebDAV)
508 ->Loop detected (WebDAv) # server is detected in infinite loop process request


HTTP ->response status codes
100 ->Continue
101 ->Switching Protocols
102 ->Processing
103 ->Early Hints
200 ->OK
201 ->Created
202 ->Accepted
203 ->Non-Authoritative Information
204 ->No Content
205 ->Reset Content
206 ->Partial Content
207 ->Multi-Status
208 ->Already Reported
226 ->IM Used
300 ->Multiple Choices
301 ->Moved Permanently
302 ->Found
303 ->See Other
304 ->Not Modified
307 ->Temporary Redirect
308 ->Permanent Redirect
400 ->Bad Request
401 ->Unauthorized
402 ->Payment Required
403 ->Forbidden
404 ->Not Found
405 ->Method Not Allowed
406 ->Not Acceptable
407 ->Proxy Authentication Required
408 ->Request Timeout
409 ->Conflict
410 ->Gone
411 ->Length Required
412 ->Precondition Failed
413 ->Content Too Large
414 ->URI Too Long
415 ->Unsupported Media Type
416 ->Range Not Satisfiable
417 ->Expectation Failed
418 ->I'm a teapot
421 ->Misdirected Request
422 ->Unprocessable Content
423 ->Locked
424 ->Failed Dependency
425 ->Too Early
426 ->Upgrade Required
428 ->Precondition Required
429 ->Too Many Requests
431 ->Request Header Fields Too Large
451 ->Unavailable For Legal Reasons
500 ->Internal Server Error
501 ->Not Implemented
502 ->Bad Gateway
503 ->Service Unavailable
504 ->Gateway Timeout
505 ->HTTP Version Not Supported
506 ->Variant Also Negotiates
507 ->Insufficient Storage
508 ->Loop Detected
510 ->Not Extended
511 ->Network Authentication Required
->







"""




"""
HTTP request methods

-> # to connect need this
CONNECT server.example.com:80 HTTP/1.1
Host: server.example.com:80
Proxy-Authorization: basic aGVsbG86d29ybGQ=
<-



-> # to delete need this
DELETE /file.html HTTP/1.1
Host: example.com

If a DELETE method is successfully applied, there are several response status codes possible:

A 202 (Accepted) status code if the action will likely succeed but has not yet been enacted.
A 204 (No Content) status code if the action has been enacted and no further information is to be supplied.
A 200 (OK) status code if the action has been enacted and the response message includes a representation describing the status.

 HTTP/1.1 200 OK
Date: Wed, 21 Oct 2015 07:28:00 GMT

<html>
  <body>
    <h1>File deleted.</h1>
  </body>
</html>

<-


-><-

-># GET
GET /index.html



<-









-># head index 

HEAD /index.html

<-




->#Identifying allowed request methods To find out which request methods a server supports, one can use the curl command-line program to issue an OPTIONS request:

The response then contains an Allow header that holds the allowed methods:

HTTP/1.1 204 No Content
Allow: OPTIONS, GET, HEAD, POST
Cache-Control: max-age=604800
Date: Thu, 13 Oct 2016 11:45:00 GMT
Server: EOS (lax004/2813)

curl -X OPTIONS https://example.org -i

<-









-># patch 
PATCH /file.txt HTTP/1.1

z.b
PATCH /file.txt HTTP/1.1
Host: www.example.com
Content-Type: application/example
If-Match: "e0023aa4e"
Content-Length: 100


<-
-># post
A simple form using the default application/x-www-form-urlencoded content type:


POST /test HTTP/1.1
Host: foo.example
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

field1=value1&field2=value2
<-





->#PUT 
PUT /new.html HTTP/1.1



PUT /new.html HTTP/1.1
Host: example.com
Content-type: text/html
Content-length: 16

<p>New File</p>
<-



-> # Track  # The HTTP TRACE method performs a message loop-back test along the path to the target resource, providing a useful debugging mechanism.
TRACE /index.html


<-
-><-














"""














