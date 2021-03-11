"""
def KelvinToFahrenheit(Temperature):
  assert (Temperature >= 0),"Colder than absolute zero!"
  return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
"""

"""
# Define a function here.
def temp_convert(var):
  try:
    return int(var)
  except ValueError as Argument:
    print("The argument does not contain numbers\n",Argument)
# Call above function here.
temp_convert("xyz")
"""

"""
def functionName( level ):
  if level <1:
    raise Exception(level)
  return level
try:
  l=functionName(-10)
  print ("level=",l)
except Exception as e:
 print ("error in level argument",e.args[0])

"""

"""
_i = 'saif'
def simpleExample():
    return int('saif')

try:
    simpleExample()
except ValueError as e:
    print(e.args)
"""

"""
def _readfile(_arg):
    try:
        fh = open(_arg, 'r')
        print('File present')
        fh.close()
    except FileNotFoundError as _ex1:
        print(_ex1.args[1])
    except PermissionError as _ex2:
        print(_ex2.args[1])
"""

""""""
class Saiferror(IOError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Saiferror("Bad hostname")
except Saiferror as e:
    print(e.args)
"""







