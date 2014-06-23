from pyparsing import *

# JSON String: se parsea utilizando la utilidad dblQuotedString de pyparsing.
# Se remueven las comillas para que no esten incluidas en el resultado.
jsonString = dblQuotedString.setParseAction(removeQuotes)

# JSON Number: es una combinacion de varias partes (concatenadas).  Las partes son:
# signo '-' para numeros negativos, el numero en si, un punto y otro numero para numeros
# de punto flotante, y por ultimo la opcion de usar notacion exponencial.
jsonNumber = Combine(Optional('-') + ('0' | Word('123456789', nums)) +
					Optional('.' + Word(nums)) +
					Optional(Word('eE', exact = 1) + Word(nums + '+-', nums)))

def convertNum(s, l, tokens):
	num = tokens[0]
	try:
		return int(num)
	except ValueError:
		return float(num)
		
jsonNumber.setParseAction(convertNum)

# JSON Object: se crea aqui, se define mas tarde.  Esto permite utilizar definiciones
# recursivas (un objeto puede estar adentro de otro objeto).
jsonObject = Forward().setResultsName('jsonObject')

# JSON Value (interno): encapsula todos los tipos de datos de JSON.  Definido mas adelante.
jsonValue = Forward() 

# JSON Elements (interno): Una lista jsonValue separados por comas.
jsonElements = delimitedList(jsonValue)

# JSON Array: se define como un jsonElements opcional, rodeado con corchetes.  El contenido es
# rodeado con Optional() ya que una lista JSON puede estar vacia.
jsonArray = Group(Suppress('[') + Optional(jsonElements) + Suppress(']')).setResultsName('jsonArray')

# JSON True, False, Null: simplemente se reemplazan las keywords de JSON 'true', 'false' y 'null' por sus
# equivalentes en Python: 'True', 'False' y 'None'.
jTrue = Keyword("true").setParseAction(replaceWith(True))
jFalse = Keyword("false").setParseAction(replaceWith(False))
jNull = Keyword("null").setParseAction(replaceWith(None))

# Se define JSON Value como cualquier tipo de valor JSON.
jsonValue << (jsonString | jsonNumber | Group(jsonObject) | Group(jsonArray) | jTrue | jFalse | jNull)

# JSON Definition (interno): Describe la definicion de un miembro en JSON.  Esto es, el nombre del objeto,
# (utilizamos jsonString ya que representa una cadena de caracteres entre comillas), un simbolo ':', y el valor
# en si.  Por ejemplo: 'a' : 1.
jsonDef = Group(jsonString + Suppress(':') + jsonValue)

# JSON Members (interno): Los miembros de un objeto son una lista de jsonDef separados por comas.
jsonMembers = delimitedList(jsonDef)

# Se termina de definir JSON Object.  Notar que jsonMembers es opcional, ya que un objeto puede estar vacio.
jsonObject << Dict(Suppress('{') + Optional(jsonMembers) + Suppress('}'))

# Finalmente, jsonRoot representa la primera parte del codigo JSON a ser parseada.  En este caso, tomamos que
# el codigo JSON pude estar enteramente contenido adentro de un objeto, o una lista.
jsonRoot = (jsonObject | jsonArray)

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