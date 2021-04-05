# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:28:31 2021

@author: Usuario
"""

def tabla(N):
    print('    ', end='')
    print('-------------------------------------------')
    for j in range(N):
        print(f'{j:>5}', end =' ')
        
        
    for x in range(N):
        
        
        valor = 0
        print()
            

        print(f'{x:>5}|', end = ' ')
        for y in range(N):
            
            print(f'{valor:>5}' ,end = '')
        
            valor = valor + x
        
print(tabla(8))
        
        

        