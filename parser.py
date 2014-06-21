from pyparsing import *

jsonString = dblQuotedString.setParseAction(removeQuotes)
jsonNumber = Combine(Optional('-') + ('0' | Word('123456789', nums)) +
					Optional('.' + Word(nums)) +
					Optional(Word('eE', exact = 1) + Word(nums + '+-', nums)))

jsonRoot = Forward()

jsonObject = Forward().setResultsName('jsonObject')

jsonValue = Forward() 

jsonElements = delimitedList( jsonValue )

jsonArray = Group(Suppress('[') + Optional(jsonElements) + Suppress(']') ).setResultsName('jsonArray')

jTrue = Keyword("true").setParseAction(replaceWith(True))
jFalse = Keyword("false").setParseAction(replaceWith(False))
jNull = Keyword("null").setParseAction(replaceWith(None))

jsonValue << (jsonString | jsonNumber | Group(jsonObject) | Group(jsonArray) | jTrue | jFalse | jNull)
jsonDef = Group(jsonString + Suppress(':') + jsonValue)
jsonMembers = delimitedList(jsonDef)
jsonObject << Dict(Suppress('{') + Optional(jsonMembers) + Suppress('}'))
jsonRoot << (jsonObject | jsonArray)

def convertNum(s, l, tokens):
	num = tokens[0]
	try:
		return int(num)
	except ValueError, ve:
		return float(num)
		
jsonNumber.setParseAction(convertNum)

def getType(res):
		if not isinstance(res, ParseResults):
			return 'Primitive', res.__class__.__name__
		
		return 'JSON', res.getName()

def parse(json):
	try:
		convertToPython(jsonRoot.parseString(json))		
	except ParseException:
		print 'Invalid JSON'

arrayCounter = 0
objectCounter = 0
tab = '\t'

def convertToPython(result):
	print('\ndef generateInstance(): ')

	rootType, rootName = getType(result)
	root = ""
	if rootName == 'jsonArray':
		root = convertJsonArray(result)
	else:
		root = convertJsonObject(result)

	print(tab + "return " + root)

def convertJsonArray(result):	
	global arrayCounter
	arrayName = 'array' + str(arrayCounter)
	arrayCounter = arrayCounter + 1
	
	print(tab + arrayName + ' = []')

	for i in result['jsonArray']:
		item = convert(i)
		print(tab + arrayName + '.append(' + item + ')')

	return arrayName


def convertJsonObject(result):
	global objectCounter
	objectName = 'object' + str(objectCounter)
	objectCounter = objectCounter + 1

	print(tab + objectName + ' = {}')

	for k, v in result['jsonObject']:
		item = convert(v)
		print(tab + objectName + '[\'' + str(k) + '\'] = ' + item)

	return objectName

def convert(result):
	classification, name = getType(result)

	if name == 'jsonArray':
		return convertJsonArray(result)
	elif name == 'jsonObject':
		return convertJsonObject(result)
	elif name == 'str':
		return "'" + result + "'"
	else:
		return str(result)