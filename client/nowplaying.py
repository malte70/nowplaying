#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Client library for NowPlaying
# 
# contains a python class and a demo client
#

APIKEY = ""

# --------
# sys for sys.exit(), and urllib to access the API (urllib2 has no
# urlencode, therefore urllib is also used.)
import sys
import urllib
import urllib2


class NowPlayingClient(object):
	"""
	Client for NowPlaying
	"""
	" The API URL "
	api_base_url = "http://np.malte70.de/api/"
	def __init__(self, api_key):
		self.api_key = api_key
		
	def sendTrack(self, interpreter, title):
		"""
		send a track to the API
		"""
		return urllib2.urlopen(
					urllib2.Request(
						self.api_base_url+self.api_key,
						urllib.urlencode({
							'interpreter': interpreter,
							'title': title
						}))
					).read()

def main():
	"""
	simple command line client.
	"""
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
		"""
		some debugging
		"""
		print "ERROR!\nServer response below:\n\n--BEGIN SERVER RESPONSE--"
		print ret
		print "--END SERVER RESPONSE--"
		sys.exit(1)

if __name__=="__main__":
	main()
