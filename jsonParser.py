# jsonParser.py
#
# Implementation of a simple JSON parser, returning a hierarchical
# ParseResults object support both list- and dict-style data access.
#
# Copyright 2006, by Paul McGuire
#
# Updated 8 Jan 2007 - fixed dict grouping bug, and made elements and
#   members optional in array and object collections
#
json_bnf = """
object 
	{ members } 
	{} 
members 
	string : value 
	members , string : value 
array 
	[ elements ]
	[] 
elements 
	value 
	elements , value 
value 
	string
	number
	object
	array
	true
	false
	null
"""

from pyparsing import *

TRUE = Keyword("true").setParseAction( replaceWith(True) )
FALSE = Keyword("false").setParseAction( replaceWith(False) )
NULL = Keyword("null").setParseAction( replaceWith(None) )

jsonString = dblQuotedString.setParseAction( removeQuotes )
#jsonString = jsonString.setResultsName('jsonString')

jsonNumber = Combine( Optional('-') + ( '0' | Word('123456789',nums) ) +
					Optional( '.' + Word(nums) ) +
					Optional( Word('eE',exact=1) + Word(nums+'+-',nums) ) )

#jsonNumber = jsonNumber.setResultsName('jsonNumber')

jsonRoot = Forward().setResultsName('jsonRoot')

jsonObject = Forward()
jsonObject = jsonObject.setResultsName('jsonObject')

jsonValue = Forward() #.setResultsName('jsonValue')

jsonElements = delimitedList( jsonValue )
#jsonElements = jsonElements.setResultsName('jsonElements')

jsonArray = Group(Suppress('[') + Optional(jsonElements) + Suppress(']') ).setResultsName('jsonArray')

jsonValue << ( jsonString | jsonNumber | Group(jsonObject)  | Group(jsonArray) | TRUE | FALSE | NULL )
memberDef = Group( jsonString + Suppress(':') + jsonValue )
#memberDef = memberDef.setResultsName('memberDef')
jsonMembers = delimitedList( memberDef )
#jsonMembers = jsonMembers.setResultsName('jsonMembers')
jsonObject << Dict( Suppress('{') + Optional(jsonMembers) + Suppress('}') )
jsonRoot << ( jsonObject | jsonArray )

jsonComment = cppStyleComment 
jsonObject.ignore( jsonComment )

def convertNumbers(s,l,toks):
	n = toks[0]
	try:
		return int(n)
	except ValueError, ve:
		return float(n)
		
jsonNumber.setParseAction( convertNumbers )
	
if __name__ == "__main__":
	testdata = """
	{
		"glossary": {
			"title": "example glossary",
			"GlossDiv": {
				"title": "S",
				"GlossList": 
					{
					"ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"TrueValue": true,
					"FalseValue": false,
					"Gravity": -9.8,
					"LargestPrimeLessThan100": 97,
					"AvogadroNumber": 6.02E23,
					"EvenPrimesGreaterThan2": null,
					"PrimesLessThan10" : [2,3,5,7],
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": "A meta-markup language, used to create markup languages such as DocBook.",
					"GlossSeeAlso": ["GML", "XML", "markup"],
					"EmptyDict" : {},
					"EmptyList" : []
					}
			}
		}
	}
	"""
	
	test2 = """
		{ "a" : "asdfas",
		  "b" : 1000000 ,
		  "c" : { "d" : 33 }, 
		  "h" : [],
		  "g" : [ 1, 1 ], 
		  "o" : null }
	"""

	def get_type(res):
		
		if res.__class__.__name__ != 'ParseResults':
			return 'Primitive', res.__class__.__name__
		
		names = [ 'jsonArray', 'jsonObject', 'jsonNumber', 'jsonString', 'jsonElements', 'jsonRoot', 'memberDef' ]
		
		for name in names:
			if name in res:
				return 'JSON', name
			
		print 'error, keys: ', res.keys()
		raise Exception('unknown parsed type')

	def get_type2(res):
		
		if not isinstance(res, ParseResults):
			return 'Primitive', res.__class__.__name__
		
		return 'JSON', res.getName()

	results2 = jsonObject.parseString(test2)
	dic2 = results2.asDict()
	
	print results2.asXML()
	
	#print results2.getName()
	rr = results2['a']
	
	print 'raiz es: ', get_type2(results2)
	
	print 'a es: ', get_type2(results2['a'])
	
	print 'b es: ', get_type2(results2['b'])
	
	print 'c es: ', get_type2(results2['c'])
	
	print 'h es: ', get_type2(results2['h'])
	
	print 'g es: ', get_type2(results2['g'])
	print 'g[0] es: ', get_type2(results2['g']['jsonArray'][0])
	
	print 'o es: ', get_type2(results2['o'])
	#test = results2['c']['memberDef']
	#print get_type2(test)
	
	#for k, v in dic2.iteritems():
	#	print k, v

	results = jsonObject.parseString(testdata)
	rdict = {}
	
	def convert(res):
		t, name = get_type(res)
		
		if t == 'Primitive':
			return res
		
		#print name
		
		res = res[name]
		
		t, name = get_type(res)
		if t == 'Primitive':
			return res
		
		if name == 'memberDef':
			res = res[name]
		
		d = {}
		for k, v in res.asDict().iteritems():
			d[k] = convert(v)
		return d
	
	#rdict = convert(results)
		
	#print rdict


