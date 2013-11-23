#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Now Playing
#
# A personal “nowplaying service” which shows the last songs you listened
# to on a website and tweets them if you want to.
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# All rights reserved.
# 
# Licensed under the terms of the 2-clause BSD license, see LICENSE for
# details.
#
# See README.md for configuration instructions.
#

###
# Configuration
CFG_BASEDIR = "/var/www/sites/np.malte70.de"
CFG_MYSQL_HOST = "localhost"
CFG_MYSQL_USER = "malte70"
CFG_MYSQL_PASSWD = "ThisIsThePassword"
CFG_MYSQL_DB = "malte70_nowplaying"
CFG_API_KEY = "ThisIsTheAPIKeyForYou"
CFG_TWITTER_ENABLED = False
CFG_TWITTER_CONSUMER_KEY = ""
CFG_TWITTER_CONSUMER_SECRET = ""
CFG_TWITTER_ACCESS_TOKEN_KEY = ""
CFG_TWITTER_ACCESS_TOKEN_SECRET = ""
# Configuration end.
###

import os,sys,time
# Change to own directory to access template files
os.chdir(CFG_BASEDIR)
# use bottle as web framework
import bottle
# for the random id of a new paste and nl2br
import string, random
# to escape the code for html output
from cgi import escape as htmlspecialchars
import MySQLdb
import twitter

# Now the magic begins. Or something like that...
npApp = bottle.Bottle()

def nl2br(text, is_xhtml = False):
	"""
	replace every newline with a <br>
	behaves like the PHP function with the same name.
	"""
	return text.replace('\n', '<br>\n') if not is_xhtml else text.replace('\n', '<br />\n')
	
@npApp.route("/")
def home():
	# get the last 6 played tracks from MySQL database
	db = MySQLdb.connect(
			host=CFG_MYSQL_HOST,
			user=CFG_MYSQL_USER,
			passwd=CFG_MYSQL_PASSWD,
			db=CFG_MYSQL_DB
			)
	db_curs = db.cursor()
	db_curs.execute("SELECT interpreter,title,link FROM log ORDER BY id DESC LIMIT 0,6;")
	db.close()
	_log = db_curs.fetchall()
	# _current is the one displayed in the jumbotron, _content contains the 5 others displayed.
	_current = ""
	if _log[0][2] != None:
		_current += "<a href=\""+_log[0][2]+"\">"
	_current = _log[0][0]+" – "+_log[0][1]
	if _log[0][2] != None:
		_current += "</a>"
	_content = '<ul class="list-group">'
	for logentry in _log[1:]:
		_content += '<li class="list-group-item">'
		if logentry[2] != None:
			_content += '<a href="'+logentry[2]+'">'
		_content += logentry[0]+' – '+logentry[1]
		if logentry[2] != None:
			_content += '</a>'
		_content += '</li>'
	_content += '</ul>'
	return bottle.template("home", title="NowPlaying :: malte70.de", current=_current,content=_content)

@npApp.route("/api/:apikey#[a-zA-Z0-9-_]+#", method="POST")
def api(apikey=None):
	# About with status 403 if the API key is wrong
	if apikey != CFG_API_KEY:
		bottle.abort(403)
	else:
		# get time and form data
		np_current_time = time.strftime('%Y-%m-%d %H:%M:%S')
		np_interpreter  = MySQLdb.escape_string(bottle.request.forms.get("interpreter"))
		np_title        = MySQLdb.escape_string(bottle.request.forms.get("title"))
		np_link         = MySQLdb.escape_string(bottle.request.forms.get("link"))
		# write track to the database
		db = MySQLdb.connect(
				host=CFG_MYSQL_HOST,
				user=CFG_MYSQL_USER,
				passwd=CFG_MYSQL_PASSWD,
				db=CFG_MYSQL_DB
				)
		db_curs = db.cursor()
		db_curs.execute("INSERT INTO log VALUES (NULL, \""+np_current_time+"\", \""+np_interpreter+"\", \""+np_title+"\", \""+np_link+"\");")
		db.commit()
		db.close()
		# if twitter is enabled, tweet the song!
		if CFG_TWITTER_ENABLED:
			api = twitter.Api(
				consumer_key=CFG_TWITTER_CONSUMER_KEY,
				consumer_secret=CFG_TWITTER_CONSUMER_SECRET,
				access_token_key=CFG_TWITTER_ACCESS_TOKEN_KEY,
				access_token_secret=CFG_TWITTER_ACCESS_TOKEN_SECRET
			)
			tweet = "#NowPlaying "+bottle.request.forms.get("interpreter")+" - "+bottle.request.forms.get("title")
			if bottle.request.forms.get("link")!=None:
				tweet += " ("+bottle.request.forms.get("link")+")"
			tweet += " via http://np.malte70.de"
			api.PostUpdate(tweet)
		return "Done.\n"

# needed for WSGI
application = npApp

