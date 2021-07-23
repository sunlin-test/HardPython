# coding:utf-8

from sys import argv

script = argv[0]
username = argv[1]
prompt = '>'

print "Hi %s, I'm the %s script." % (username, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where do you live %s?" % username
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)