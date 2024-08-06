# NUMEROS PARES

"""
def par_impar():
   numero = int(input("ingrese un numero"))
   if numero %2 == 0:
      print("tu numero: ",numero, " es par")
   else: 
      print("tu numero: ",numero, " es impar")
   return numero
par_impar()
"""


# CALCULADORA DE EDAD
"""      
def calculadora_de_edad():
    nacimiento = int(input("introduzca su año de nacimiento: "))
    año = int(input("introduzca un año para calcular su edad en ese año: "))
    calculadora = año - nacimiento
    if calculadora < 0:
     print("todavia no habias nacido")
    else:  
     print("tu edad seria: ",calculadora)
calculadora_de_edad()
"""


# ARITMETICA BASICA
"""
def matematica():
 
 numero1 = int(input("inserte su primer numero entero"))
 numero2 = int(input("inserte su segundo numero entero"))
 
 suma = numero1 + numero2 
 resta = numero1 - numero2
 multiplicacion = numero1 * numero2
 division = numero1 // numero2
 resto= numero1 % numero2
 aritmetica = suma,resta,multiplicacion,division,resto
 return aritmetica
resultado = matematica()
print("su resultado es: ",resultado )
"""

# CONCATENAR

"""
cadena1 = "Hola"
cadena2 = "mundo"
resultado = cadena1 + " " + cadena2
print(resultado)

nombre = "Juan"
edad = 30
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)

nombre = "María"
edad = 25
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)

cadena = "Hola"
repeticiones = 3
resultado = cadena * repeticiones
print(resultado)
"""

# CALCULADORA DE NUMEROS PRIMOS

"""
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def imprimir_primos(numero):
    print("Números primos hasta", numero, ":")
    for i in range(2, numero + 1):
        if es_primo(i):
            print(i, end=" ")

numero = int(input("Ingrese un número entero: "))
imprimir_primos(numero)
"""
# SUMA DE DOS ENTEROS CON CONDICIONALES

"""
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))
resultado = numero1 + numero2 
falta = 100 - resultado 
if  resultado < 100:
 print("falta: ",falta, " para llegar a 100")   
else: 
 resultado >= 100
 print("llega a 100")
 """

# ITERACION DE CUMPLEAÑOS

"""
edad = int(input("ingrese su edad: "))

def saludo_cumpleaños(edad):
    for _ in range (edad):
     print("feliz cumpleaños")
saludo_cumpleaños(edad)
"""
# LISTAS

"""
numeros = [1,2,3,4,5,6,7,8,9,10]

print("el numero de la posicion 4 de la lista es: ",numeros[4],)

longitud = len(numeros)

print("la longitud de la lista es: ",longitud,)
"""