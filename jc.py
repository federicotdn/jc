from parser import *
import sys, urllib2

def main():

	if len(sys.argv) != 3:
		error('Invalid argument.', 1)

	if sys.argv[1] == '-f':
		readFromFile()
	elif sys.argv[1] == '-u':
		readFromURL()
	else:
		error('Invalid command.', 2)

def readFromFile():
	try:
		f = open(sys.argv[2], "r")
		parse(f.read())
		f.close()
	except IOError:
		error('Unable to open file.', 3)

def readFromURL():
	try: 
		json = urllib2.urlopen(sys.argv[2]).read()
		parse(json)
	except (ValueError, urllib2.URLError):
		error('Invalid URL.', 4)

def error(msg, code):
	sys.stderr.write('Error: ' + msg + '\n')
	exit(code)

if __name__ == '__main__':
	main()