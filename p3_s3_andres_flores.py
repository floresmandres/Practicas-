# -*- coding: utf-8 -*-
"""P3_S3_andres_flores

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w62Yk8YMlBNXoQg4m0ZaPuXaxK_Oex9k
"""

#Práctica 3. Sección 3. Andres Flores V-26.223.455

#Ejercicio 1
n=11

while n <= 11:
  if n ==0 :
    break
  print(n)
  n= n-1

#Ejercicio 2
for i in range(3):
  try:
    number_1=int(input("Ingrese un número entero: "))
    acum=number_1

    while not number_1==0:
      number_1=number_1-1
      acum=acum+number_1
      if number_1==0:
        print("El resultado es: ", acum)
  except ValueError:
    print("Ha introducido un valor erróreo, inténtelo nuevamente")
  else:
    print("Gracias por preferirnos, vuelve pronto")
    break