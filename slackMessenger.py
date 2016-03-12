import urllib2, urllib
import json

##################################
# Written by Harrison Beachey 2016
#
# You can use this class to send slack messages to any channel or user
# The bot can change it's username/icon to suit its current use
#
# == !! Note !!
# After a sucessful send() call, all attachments are cleared!
#
# ==== Basic Message =======
#
# s = SlackMessenger()
# s.send("Message")
#
# ==== Full usage =======
#
# s = SlackMessanger("#random", "TrollBot", ":troll:")
# entries = {
# 	"This is a title": "This is a value",
# 	"Second Title": "Second Value",
# }
#
# s.addAttatchment("YouAttach", entries=entries)
# s.addAttatchment("MeAttach", COLOR_BLUE, "Outside the block", "Inisde the block", entries)
#
# s.send("I want to say something before the rest of this message here")
#
##################################

SLACK_URL = "https://hooks.slack.com/services/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"

COLOR_GREEN="#36a64f"
COLOR_RED="#ff5151"
COLOR_BLUE="#444fd7"

def inlineFormat(text):
		return "`" + text + "`"

def blockFormat(text):
	return "```" + text + "```"

def linkFormat(text, link):
	return "<" + link + "|" + text + ">"

class SlackMessanger(object):
	def __init__(self, channel=None, username=None, icon=None):
		self.hookUrl     = SLACK_URL
		self.channel     = channel
		self.username    = username
		self.icon        = icon
		self.attachments = []
		self.debug       = False

	def addAttatchment(self, summery, color=None, outsideBlock=None, insideBlock=None, entries={}):
		newAttatch = {
				"fallback": summery,
				"pretext": outsideBlock or summery,
				"text": insideBlock,
				"color": color,
				"fields": [{"title": k, "value": v} for k,v in entries.iteritems()]
			}

		self.attachments.append(newAttatch)

	def send(self, summery=None):
		data = {
			"channel": self.channel,
			"username": self.username,
			"text": summery,
			"attachments": self.attachments
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
				self.attachments = []
		except Exception, e:
			print "Error sending message to slack!"
			print e
