from parser import *

def main():

	test = """
		[{ "a" : "asdfas",
				  "b" : 1000000 ,
				  "c" : { "d" : 33 }, 
				  "h" : [],
				  "g" : [ 1, 1 ], 
				  "o" : null }]
	"""
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
	parse(testdata)


if __name__ == '__main__':
	main()