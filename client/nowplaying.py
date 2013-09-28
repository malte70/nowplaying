#!/usr/bin/env python2
# -*- coding: utf-8 -*-

APIKEY = ""

# --------
import sys
import string
import urllib
import urllib2


class NowPlayingClient(object):
	api_base_url = "http://np.malte70.de/api/"
	def __init__(self, api_key):
		self.api_key = api_key
		
	def sendTrack(self, interpreter, title):
		return urllib2.urlopen(
					urllib2.Request(
						self.api_base_url+self.api_key,
						urllib.urlencode({
							'interpreter': interpreter,
							'title': title
						}))
					).read()

def main():
	if len(sys.argv)!=3:
		print "usage: nowplaying \"Interpreter\" \"Title\""
		sys.exit(1)
	interpreter = sys.argv[1]
	title = sys.argv[2]
	
	global APIKEY
	client = NowPlayingClient(APIKEY)
	ret = client.sendTrack(interpreter, title)
	if ret == "Done.\n":
		sys.exit(0)
	else:
		print "ERROR!\nServer response below:\n\n--BEGIN SERVER RESPONSE--"
		print ret
		print "--END SERVER RESPONSE--"
		sys.exit(1)

if __name__=="__main__":
	main()
