# Requests module

https://docs.python-requests.org/en/master/api/
requests has these request types
    GET - retrieve info
    POST - server accepts the data in the body
    PUT - store under the URI
    DELETE - deletes the resource
    HEAD - same as GET but without the response body
    PATCH - modify a resource, but only needs to provide what is new

and these arguments
method - requests if you dont specify with the function call (requests.request('GET', url))
    url
    params - dict, list of tuples or bytes to send the query string
    data - dict, list of tuples, bytes, or file-like object to send in the body
    json - a JSON serializable python object to send in the body
    headers - dict HTTP header to send with the request
    cookies - dict or CookieJar object
    files - 
        dict for multipart encoding:
            {'name': file-like-objects}
            {'name': file-tuple}
        file-tuple
            ('filename', fileobj)
            ('filename', fileobj, 'content_type')
            ('filename', fileobj, 'content_type', custom_headers)
            where content_type is a string defining the content type of the file
            custom_headers is a dict like object containing additional headers to add
    auth - basic/digest/custom HTTP auth
    timeout - float or tuple for how many seconds to wait for the server to send data
    allow_redirects - [True/False] defaults to True
    proxies - dict mapping protocol to the URL of the proxy
    verify - boolean to check servers TLS certificate or a string path to a CA bundle to use. defaults to True
    stream - if False the response content will be downloaded
    cert - str path to ssl client cert file or tuple ('cert', 'key')

