from random import randint
from random import shuffle
import os
import re
import methods 

def createListCase(min, max):    
    range_nums = randint(0, max) 
    better_case = [num for num in range(range_nums - min, range_nums)]
    average_case = [num for num in range(range_nums - min, range_nums)]
    shuffle(average_case)
    worse_case = [num for num in range(range_nums - min, range_nums)]
    worse_case.sort(reverse=True) 
    
    return better_case, average_case, worse_case  

def generalTest():
    pass

def individualTest():
    pass

if __name__ == "__main__":
    
    # Caso de 10 elementos
    better_case, average_case, worse_case = createListCase(10,100)
    case_10elements = [better_case, average_case, worse_case]
        
    # Caso de 100 elementos
    better_case, average_case, worse_case = createListCase(100, 1000)
    case_100elements = [better_case, average_case, worse_case]
        
    # Caso de 1000 elementos
    better_case, average_case, worse_case = createListCase(1000, 10000)
    case_1000elements = [better_case, average_case, worse_case]
    
    endProgram = False
    while not endProgram:
        print("//MEDIDOR DE ALGORITMOS//\n"
              "a) Iniciar pruebas generales\n"
              "b) Iniciar pruebas individuales\n"
              "c) Cerrar")
        option_selected = input("[INGRESE UNA OPCION]")
               
        if option_selected in 'a':
            generalTest()
        elif option_selected in 'b':
            individualTest()
        elif option_selected in 'c':
            endProgram = True
        else:
            print("[*] WARNING: Ingrese un caracter valido")
        os.system("cls")
            
      
        
        
        
        
    