import urllib2, urllib
import json

from keys import SLACK_URL

##################################
# Written by Harrison Beachey 2016
#
# You can use this class to send slack messages to any channel or user
# The bot can change it's username/icon to suit its current use
#
# == !! Note !!
# After a sucessful send() call, all blocks are cleared!
#
# ==== Basic Message =======
#
# s = SlackMessenger()
# s.send("Message")
#
# ==== Full usage =======
#
# s = SlackMessenger("#random", "TrollBot", ":troll:")
# entries = {
# 	"This is a title": "This is a value",
# 	"Second Title": "Second Value",
# }
#
# s.addColorBlock("YouAttach", entries=entries)
# s.addColorBlock("MeAttach", COLOR_BLUE, "Outside the block", "Inisde the block", entries)
#
# s.send("I want to say something before the rest of this message here")
#
##################################

COLOR_GREEN="#36a64f"
COLOR_RED="#ff5151"
COLOR_BLUE="#444fd7"

def inlineFormat(text):
		return "`" + text + "`"

def blockFormat(text):
	return "```" + text + "```"

def linkFormat(text, link):
	return "<" + link + "|" + text + ">"

class SlackMessenger(object):
	def __init__(self, channel=None, username=None, icon=None):
		self.hookUrl     = SLACK_URL
		self.channel     = channel
		self.username    = username
		self.icon        = icon
		self.blocks      = []
		self.debug       = False

	def addColorBlock(self, summery, color=None, outsideBlock=None, insideBlock=None, entries={}):
		newBlock = {
				"fallback": summery,
				"pretext": outsideBlock or summery,
				"text": insideBlock,
				"color": color,
				"fields": [{"title": k, "value": v} for k,v in entries.iteritems()]
			}

		self.blocks.append(newBlock)

	def send(self, summery=None):
		data = {
			"channel": self.channel,
			"username": self.username,
			"text": summery,
			"attachments": self.blocks
		}

		if self.icon:
			if self.icon[0] == ':':
				data["icon_emoji"] = self.icon
			else:
				data["icon_url"] = self.icon

		sendData = json.dumps(data)

		if self.debug:
			print sendData

		try:
			req = urllib2.Request(self.hookUrl, sendData)
			response = urllib2.urlopen(req)
			result = response.read()

			if result == "ok":
				channel = self.channel or "#automation"
				username = self.username or "ScriptKitty"
				print 'Sent message to slack channel %s as user %s' % (channel, username)	
				self.blocks = []
		except Exception, e:
			print "Error sending message to slack!"
			print e
