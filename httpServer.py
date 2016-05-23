#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

PORT = 9001
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print 'Starting HTTP server'
httpd.serve_forever()
