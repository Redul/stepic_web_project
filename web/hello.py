def app(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  body = [bytes('\n'.join(environ['QUERY_STRING'].split('&')),
                  encoding="ascii")]
  return body
