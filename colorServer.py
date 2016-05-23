#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from gpiozero import RGBLED
from gpiozero import PWMLED

import os
import SocketServer

POWERLED = PWMLED(18,True,1)
RGB = RGBLED(22,23,24,False,(0.1,0.1,0.1))

def loadAndShowColor(color):
    divider     = 256

    red         = float(int("0x"+color[0:2], 0))

    green       = float(int("0x"+color[2:4], 0))
    green       = green-(green/2.5)

    blue        = float(int("0x"+color[4:6], 0))

    if red>=divider:
       red=divider
    if green>=divider:
       green=divider
    if blue>=divider:
       blue=divider

    RGB.red      = red/divider
    RGB.green    = green/divider
    RGB.blue     = blue/divider
    return

class S(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        color = self.rfile.read(length).decode('utf-8')[:6]
        loadAndShowColor(color)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

def run(server_class=HTTPServer, handler_class=S, port=9000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting color server'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
