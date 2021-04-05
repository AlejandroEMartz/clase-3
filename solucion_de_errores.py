# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 00:03:40 2021

@author: Usuario
"""
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo Semántico y estaba ubicado en la expresión del if 
# y tambien al excluir las a Mayusculas
#    Lo corregí cambiando el i == "a" por "a" in expresion  y agregando una expresion.lower()
#    A continuación va el código corregido



def tiene_a(expresion):
    
    n = len(expresion)
    print(n)
    i = 0
   
   
    while i <= n:
        
         if expresion.isupper() == True:
             expresion = expresion.lower()
        
         if 'a' in expresion :
            return True
         else:
            return False
         i += 1



print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintaxis tipo y estaba ubicado en la falta de dos puntos
#en el while, en el if,  en el operador logico =, Y en el operador False que estaba 
#escrito como Falso
#A continuación va el codigo corregido


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' :
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de tipo SINTAXIS y estaba ubicado en la forma en
#que fue ingresado el nro 1984 como int, que impedia que se hiciera len()

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))






