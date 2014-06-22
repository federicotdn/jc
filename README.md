##TPE Teoría de Lenguajes y Autómatas: jc

###Requerimientos:

Para utilizar el proyecto, es necesario tener instalado un intérprete de Python 2.7.  El proyecto fue probado
en CPython (la implementación estandar de Python), y PyPy, un intérprete/compilador JIT que permite correr codigo
Python con mayor velocidad.  Se recomienda utilizar PyPy ya que provee una mejor velocidad que CPython, especialmente
cuando se procesan archivos JSON de gran tamaño.

###Invocación:

Utilizando un archivo como parámetro:

pypy jc.py -f nombrearchivo

Utilizando una URL:

pypy jc.py -u urlvalida

Para guardad el código generado, se puede utilizar redirección de salida.  En bash:

pypy jc.py -f sample.json > generado.py