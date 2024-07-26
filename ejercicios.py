
# N = int(input("Digite un numero de terna: "))


# for t in range(N):
#     print("Digite los valor de la terna t: ", t+1, "De :", N)
#     x = int(input("digite el valor de x :"))
#     y = int(input("digite el valor de y :"))
#     z = int(input("digite el valor de z :"))

#     if (x == y) or (x == z) or (y == z):
#         print("Hay dos iguales")

#     elif x > y and y > z:
#         print("El mayor es X: ", x)
#         print("El menor es z: ", z)

#     elif x > z and z > y:
#         print("El meyor es x: ", x)
#         print("El menor es y: ", y)

#     elif y > x and x > z:
#         print("El meyor es x: ", y)
#         print("El menor es z: ", z)


#     elif y > z and z > x:
#         print("El mayorr es y: ", y)
#         print("El menor es x: ", x)

#     elif z > x and x > y:
#         print("El mayor es z: ", z)
#         print("El menor es y: ", y)

#     else:
#         if z > y and y > x:
#             print("El mayor es z: ", z)
#             print("El menor es x: ", x)
#     print("Fin del programa")

# norte = int(input("Digita un numero: "))
# print(norte >= 100)

# encontramos el mayor de los tres números..
# Se leen tres números

# N = int(input("Digite un numero de terna: "))

# for t in range(N):
#     print("Digite los valor de la terna t: ", t+1, "De :", N)
#     number1 = int(input("Ingresa el primer número: "))
#     number2 = int(input("Ingresa el segundo número: "))
#     number3 = int(input("Ingresa el tercer número: "))
#     number4 = int(input("Ingresa el cuarto número: "))
#     number5 = int(input("Ingresa el quinto número: "))
#     number6 = int(input("Ingresa el sexto número: "))


#     if (number1 == number2) or (number1 == number3) or (number2 == number3):
#         print("Hay dos iguales")
#     # Asumimos temporalmente que el primer número
#     # es el más grande.
#     # Lo verificaremos pronto.
#     largest_number = number1

#     # Comprobamos si el segundo número es más grande que el mayor número actual
#     # y actualiza el número más grande si es necesario.
#     if number2 > largest_number:
#         largest_number = number2

#     # Comprobamos si el tercer número es más grande que el mayor número actual
#     # y actualiza el número más grande si es necesario.
#     if number3 > largest_number:
#         largest_number = number3

#     if number4 > largest_number:
#         largest_number = number4

#     if number5 > largest_number:
#         largest_number = number5

#     if number6 > largest_number:
#         largest_number = number6
# # Imprime el resultado.
#     print("El número más grande es:", largest_number)

# El código debe mostrar uno de los dos mensajes posibles, que sonAño BisiestoohAño Común

# year = int(input("Introduce un año: "))

# if year < 1582:
#     print("No esta dentro del período del calendario Gregoriano")
# else:
#     if year % 4 != 0:
#         print("Año Común")
#     elif year % 100 != 0:
# #         print("Año Bisiesto")
# #     elif year % 400 != 0:
# #         print("Año Común")
# #     else:
# #         print("Año Bisiesto")


# # # Almacena el actual número más grande aquí.
# # largest_number = -999999999

# # # Ingresa el primer valor.
# # number = int(input("Introduce un número o escribe -1 para detener: "))

# # # Si el número no es igual a -1, continuaremos
# # while number != -1:
# #     # ¿Es el número más grande que el valor de largest_number?
# #     if number > largest_number:
# #         # Sí si, se actualiza largest_number.
# #         largest_number = number
# #     # Ingresa el siguiente número.
# #     number = int(input("Introduce un número o escribe -1 para detener: "))

# # # Imprime el número más grande.
# # print("El número más grande es:", largest_number)


# # Un programa que lee una secuencia de números
# # y cuenta cuántos números son pares y cuántos son impares.
# # El programa termina cuando se ingresa un cero.

# odd_numbers = 0
# even_numbers = 0

# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))

# # # Imprimir resultados.
# # print("Conteo de números impares:", odd_numbers)
# # print("Conteo de números pares:", even_numbers)

# # i = 1
# # while i < 5:
# #     print(i)
# #     i += 1
# # else:
# #     print("else:", i)

# #Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
# blocks = int(input("Enter the number of blocks: "))

# height = 0

# inlayer = 1

# while inlayer <= blocks:

#     height += 1
#     blocks -= inlayer  # Esta línea de código funciona distinto a la de arriba y abajo?
#     inlayer += 1

# print("The height of the pyramid: ", height)
# # Esta es una lista existente de números ocultos en el sombrero.
# hat_list = [1, 2, 3, 4, 5]

# # Paso 1: escribe una línea de código que solicite al usuario
# num = int(input("Digite un numero: "))
# # reemplazar el número de en medio con un número entero ingresado por el usuario.

# lista = [2, 5, 6, 5, 4, 6,]
# acum = 0
# for i in range(len(lista)):
#     acum += lista[i]
# print(acum)
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)
# hat_list[2] = num

# # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
# del hat_list[4]

# # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

# print("\nla longitud de la lista es_", len(hat_list))

# nota = [1, 5, 5, 6, 7,]
# nota.sort()
# print(nota)

# x = []
# x.append(100)
# x.append(-1)
# x.sort()
# print(x)

# cod = []
# nom = []
# nota1 = []
# nota2 = []
# defi = []
# sumadefi = 0

# for i in range(4):
#     codigo = input("Digite su codigo: ")
#     cod.append(codigo)
#     nombre = input("Digite su nombre: ")
#     nom.append(nombre)
#     n1 = float(input("Digite la nota1 : "))
#     nota1.append(n1)
#     n2 = float(input("digite la nota2: "))
#     nota2.append(n2)
#     definitiva = (n1+n2)/2
#     sumadefi += definitiva
#     defi.append(definitiva)
# print("Imprimo despues del for i:")

# promG = sumadefi/4
# print()
# conta = 0
# for x in range(4):
#     if defi[x] >=promG:
#         conta+=1
#     print(cod[x], nom[x], defi[x])
#     print()
#     print("Numero de estudiante con difinitivas >= promedio del grupo ,",conta)
# print("promedio del grupo =====>  ", promG)

# valor mayor en la lista:
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

# Cubo - un arreglo tridimensional (3x3x3)
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

# nom = input("digite el nombre: ")

# apell1 = input("Digite el apellido: ")
# apell2 = input("Digite el apellido2: ")

# inicia = nom[0]
# inicia = inicia+apell1[0]
# inicia = inicia+apell2[0]

# print("las iniciales del apelledio son: ", inicia)

# N = int(input("Digite el factorial: "))
# i = 1
# factorial = 1
# while i <= N:
#     factorial = factorial*i
#     i = i+1
# print("El factorial de :", N, "es: ", factorial)
# print()

# x = int(input("digite el factorial: "))
# i = 1
# factorial = 1
# while i <= x:
#     factorial = factorial*i
#     i += 1
# print("el factorial de : . ", x, "es:", factorial)

# x = int(input("DIGITE el factoria: "))
# factorial = 1
# for i in range(1, x+1):
#     factorial *= i
# print("el factorial de : . ", x, "es:", factorial)

# x = int(input("digite un numero: "))
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print("el factorial de : . ", x, "es:", factorial)

# import random
# intentos = 10
# num_secreto = random.randint(1, 100)
# num_ingresado = int(input("Adivine el numero (de 1 a 100):"))

# while num_secreto != num_ingresado and intentos > 1:
#     if num_secreto > num_ingresado:
#         print("Muy bajo")
#     else:
#         print("Muy alto")
#     intentos = intentos-1
#     print("Le quedan ", intentos, " intentos:")
#     num_ingresado = int(input("Adivine el numero (de 1 a 100):"))

# if num_secreto == num_ingresado:
#     print("Exacto! Usted adivino en ", 11-intentos, " intentos.")
# else:
#     print("El numero era: ", num_secreto)

# n = 3
# m = 4
# matriz = []
# for i in range(n):
#     matriz.append([0]*m)
# print(matriz)
# for f in range(n):
#     for c in range(m):
#         matriz[f][c] = float(input("digite un valor: \n"))
# print(matriz)

# nf = 4
# nc = 2

# personas = []
# for f in range(nf):
#     personas.append([""]*nc)
# for f in range(nf):
#     print(personas[f])
# for f in range(nf):
#     print("Digite los datos Personales: "

# frut = ["mango", "pera", "lulo"]
# for i in frut:
#     print(i)
# print(frut[1:])

# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)

# dictionary = {"gato": "chat",
#               "perro": "chien",
#               "caballo": "cheval"}
# phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)

# dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
# words = ['gato', 'león', 'caballo']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
# print(word, "no está en el diccionario")


# dictionary = {"gato": "chat",
#               "perro": "chien",
#               "caballo": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# for spanish, french in dictionary.items():
#     print(spanish, "->", french)

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)


# print(f(3))


# def fun(x):
#     x += 1
#     return x


# x = 2
# x = fun(x + 1)
# print(x)

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])

# def func(a, b):
#     return a ** a


# print(func(2))

# def func_1(a):
#     return a ** a


# def func_2(a):
#     return func_1(a) * func_1(a)


# print(func_2(2))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)

# def fun(x):
#     global y
#     y = x * x
#     return y


# fun(2)
# print(y)

# def any():
#     print(var + 1, end='')


# var = 1
# any()
# print(var)

# my_list = ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))

# def fun(x, y, z):
#     return x + 2 * y + 3 * z


# print(fun(0, z=1, y=3))

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# try:
#     value = input("Ingresa un valor: ")
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except TypeError:
#     print("Entrada muy errónea...")
# except:
#     print("¡Buuu!")

# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)
# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))

# print(1//2)
# def func(a, b):
#     return b ** a


# print(func(b=2, 2))
# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y
# print(x)

# my_list = [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2


# print(fun(fun(2)))

# nums = [1, 2, 3]
# vals = nums
# del vals[:]

# print(nums)
# print(vals)
# x = int(input("digite un valor: "))
# y = int(input("digite un valor: "))
# x = x % y
# x = x % y
# y = y % x
# print(y)

# print("a", "b", "c", sep="sep")

# x = 1 // 5 + 1 / 5
# print(x)

# x = float(input("digirte"))
# y = float(input("digite "))
# print(y ** (1 / x))

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]
# pedir la masa en kilogramos
# masa=float(input("Digite la masa en kilogramos: "))
# #calcular la ecuacioón de e =m*c
# c=300000
# energia= masa=c*c
# print("la energia es igual es: ",energia, "Julio")


#Maquina expendedora
# precio=50
# denominaciones=[25,10,5]
# contador=0
# adeudado= precio

# while adeudado >=0:
#     moneda = int(input("Ingresa una monenda: (25, 10, 5): "))
#     if moneda in denominaciones:
#         contador +=moneda
#         adeudado -=moneda
#         print("Monto adeudado: {} centavo",format(adeudado))
#     else:
#         print("moneda no aceptada. ingrese una moneda de 25,10,5, centavos")
# if contador>precio:
#     cambio= contador-precio
#     print("cambio: { ccentavos}",format(cambio))
#Ejercicio 3
# Usuario =input("Digite el nombres: ")
# print(f"!Hola {Usuario}!")
# print()

# # #Ejercicio 4
# # print(((3+2)/(2*5))**2)
# # print()
# #Ejercicio 5
# nombre =input("Digite el nombres: ")
# hora=float(input("Cuantas horas trabajo: "))
# costo=float(input("caunto el el valor de la hora: "))
# totalP= hora*costo
# print(f"Hola: {nombre} el valor a paEl valor a pagar es: {totalP}")
# print()
# #Ejercicio 6
# n=int(input("Digita un numero entero:  "))
# suma =n*(n+1)/2
# print(f"La suma de los numero desde  1  hasta {n} es {suma}")
# print()
# #Ejercicio 7
# peso=float(input("Digite su peso : "))
# estatura=float(input("Digite su estatura : "))
# imc=peso/(estatura)**2
# print(f"Tu indice de masa es:{round(imc),2} ")



