# -*- coding: utf-8 -*-
"""work_class_fubonacci

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TJzkYRnyAwTK146LpjgkvDgQoxmxofkg
"""

#EJERCICIO 1 SERIE DE FUBONACCI

N= int(input("Ingrese un numero natural, mayor a 1: "))
fib_list=[1,1]


while N<1: 
  N=int(input("El numero ingresado no es valido, intentelo nuevamente: "))

while fib_list[-1] < N:
  fib_list.append(fib_list[-2]+fib_list[-1])

if fib_list[-1] > N: 
  fib_list.pop(-1)
  print("La serie de fibonacci es: ", fib_list)

else:
  print("La serie de fibonacci es: ", fib_list)

#EJERCICIO 2 SUMA DE LA SERIE DE FUBONACCI

N= int(input("Ingrese un numero natural, mayor a 1: "))
fib_list=[1,1]
result=0

while N < 1: 
  N=int(input("El numero ingresado no es valido, intentelo nuevamente"))

while fib_list[-1] <= N:
    fib_list.append(fib_list[-2]+fib_list[-1])

if fib_list[-1] > N: 
  fib_list.pop(-1)

for i in fib_list:
  result= result + i

print("La suma de fibonacci es: ", result)

#EJERCICIO 3 SUMA DE LOS IMPARES


N= int(input("Ingrese un numero natural, mayor a 1: "))
fib_list=[1,1]
suma_impar=0

while N < 1: 
  N=int(input("El numero ingresado no es valido, intentelo nuevamente"))

while fib_list[-1] < N:
    fib_list.append(fib_list[-2]+fib_list[-1])

if fib_list[-1] > N: 
  fib_list.pop(-1)

for i in fib_list:
  if not i % 2 == 0:
    suma_impar= suma_impar + i

print("La suma de los impares de fibonacci es: ", suma_impar)

#EJERCICIO 3 Suma de los primos


N= int(input("Ingrese un numero natural, mayor a 1: "))
fib_list=[1,1]
suma_primos= 0
primo_base_5= 2 + 3 + 5
while N < 1: 
  N=int(input("El numero ingresado no es valido, intentelo nuevamente"))


while fib_list[-1] < N:
    fib_list.append(fib_list[-2]+fib_list[-1]) 

if fib_list[-1] > N: 
  fib_list.pop(-1) 

fib_list.pop(0)
fib_list.pop(0) 

for i in fib_list:
  if N<=5 :
    suma_primos= suma_primos + i
    
  elif ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0)) :
    suma_primos= suma_primos + primo_base_5 + i


print("La suma de los numeros primos de fibonacci es: ", suma_primos)