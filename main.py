from random import randint
from random import shuffle
from models.data import dataElement, case
import os
import re
import models.methods as methods 

# Varibles globales
warning = "[*] WARNING: "
output_count = "[TIEMPO] => "
results_title = "//RESULTADOS//"
error = "[!] ERROR: "

'''FUNCIONES PARA APLICAR TEST'''
def applyTest(results_method, method_function, data_10elements, data_100elements, data_1000elements):
   
    # Guardar resultados de lista de 10
    results_method.getData10().setAllAttributes(
    methods.method_function(data_10elements[0]), 
    methods.method_function(data_10elements[1]),
    methods.method_function(data_10elements[2]))
        
    #Guardar resultados de lista de 100
    results_method.getData10().setAllAttributes(
    methods.method_function(data_100elements[0]), 
    methods.method_function(data_100elements[1]),
    methods.method_function(data_100elements[2]))
    
    # Guardar resultados de lista de 1000
    results_method.getData10().setAllAttributes(
    methods.method_function(data_1000elements[0]), 
    methods.method_function(data_1000elements[1]),
    methods.method_function(data_1000elements[2]))

def applyAllTest(data_10elements, data_100elements, data_1000elements):
    bubble = dataElement()
    bubble.setName("Bubble sort")
    applyTest(bubble, methods.bubble_sort, data_10elements, data_100elements, data_1000elements)
    
    insertion = dataElement()
    applyTest(insertion, methods.insertion_sort, data_10elements, data_100elements, data_1000elements)
    insertion.setName("Insertion sort")
    
    quick = dataElement()
    applyTest(bubble, methods.quicksort, data_10elements, data_100elements, data_1000elements)
    quick.setName("Quick sort")
    
    selection = dataElement()
    applyTest(bubble, methods.selection_sort, data_10elements, data_100elements, data_1000elements)
    selection.setName("Selection sort")
    
    shell = dataElement()
    applyTest(bubble, methods.shellShort, data_10elements, data_100elements, data_1000elements)
    insertion.setName("Shell sort")
    
    shaker = dataElement()
    applyTest(bubble, methods.shakerSort, data_10elements, data_100elements, data_1000elements)
    shaker.setName("Shaker sort")
    
    return [bubble, insertion, quick, selection, shell, shaker]

'''FUNCIONES PARA MOSTRAR TESTS'''
def showIndividualResults(results_method):
    print(f"<{results_method.getName()}>")
   
    print(results_title + 
        "\n>> Lista de 10 elementos:")       
    print(output_count + f"Mejor caso {results_method.getData10().getBetterCase()}")        
    print(output_count + f"Caso promedio {results_method.getData10().getAverageCase()}")
    print(output_count + f"Peor caso {results_method.getData10().getWorseCase()}")
    print("---------------------------------------------------------")
    
    print(results_title + 
        "\n>> Lista de 10 elementos:")       
    print(output_count + f"Mejor caso {results_method.getData100().getBetterCase()}")        
    print(output_count + f"Caso promedio {results_method.getData10().getAverageCase()}")
    print(output_count + f"Peor caso {results_method.getData100().getWorseCase()}")
    print("---------------------------------------------------------")
    
    # Imprimir resultados de lista 1000
    print(results_title + 
        "\n>> Lista de 10 elementos:")       
    print(output_count + f"Mejor caso {results_method.getData100().getBetterCase()}")        
    print(output_count + f"Caso promedio {results_method.getData10().getAverageCase()}")
    print(output_count + f"Peor caso {results_method.getData100().getWorseCase()}")
    print("---------------------------------------------------------")            
    
def showGeneralResults(method_list):
    print("//RESULTADOS GENERALES//")
    
    for i in range(len(method_list)):
        print(f"<{method_list[i].getName()}>")
        showIndividualResults(method_list[i])
        
        
'''FUNCIONES PARA EJECUTAR TEST'''
def individualTest(data_10elements, data_100elements, data_1000elements):
    while True:
        results_method =  dataElement()
        
        print("//MEDIDOR DE ALGORITMOS//\n"
              "a) bubble\n"
              "b) Insertion\n"
              "c) Quicksort\n"
              "d) Selection\n"
              "e) ShellShort\n"
              "f) ShakerSort\n"
              "g) Cerrar")
        option_selected = input("[INGRESE UNA OPCION]")
        
        if option_selected in 'a':
            applyTest(results_method, methods.bubble_sort, data_10elements, data_100elements, data_1000elements)
            results_method.setName("Bubble sort")
            showIndividualResults(results_method)
            
        elif option_selected in 'b':
            applyTest(results_method, methods.insertion_sort, data_10elements, data_100elements, data_1000elements)
            results_method.setName("Insertion sort")
            showIndividualResults(results_method)
            
        elif option_selected in 'c':
            applyTest(results_method, methods.quicksort, data_10elements, data_100elements, data_1000elements)
            results_method.setName("Quick sort")
            showIndividualResults(results_method)
            
        elif option_selected in 'd':
            applyTest(results_method, methods.selection_sort, data_10elements, data_100elements, data_1000elements)
            results_method.setName("Selection sort")
            showIndividualResults(results_method)
            
        elif option_selected in 'e':
            applyTest(results_method, methods.shellShort, data_10elements, data_100elements, data_1000elements)
            results_method.setName("Shellshort")
            showIndividualResults(results_method)
            
        elif option_selected in 'f':
            applyTest(results_method, methods.shakerSort, data_10elements, data_100elements, data_1000elements)
            results_method.setName("Shaker sort")
            showIndividualResults(results_method)
            
        elif option_selected in 'g':
            break
        else:
            print(warning + "Ingrese un caracter valido") 
        enterToContinue()      

def generalTest(data_10elements, data_100elements, data_1000elements):
    method_list = applyAllTest(data_10elements, data_100elements, data_1000elements)

def enterToContinue():
    input("[INGRESE ENTER PARA CONTINUAR]")
    os.system('cls')

def createListCase(min, max):    
    range_nums = randint(0, max) 
    better_case = [num for num in range(range_nums - min, range_nums)]
    average_case = [num for num in range(range_nums - min, range_nums)]
    shuffle(average_case)
    worse_case = [num for num in range(range_nums - min, range_nums)]
    worse_case.sort(reverse=True) 
    
    return better_case, average_case, worse_case  

if __name__ == "__main__":
    
    # Caso de 10 elementos
    better_case, average_case, worse_case = createListCase(10,100)
    data_10elements = [better_case, average_case, worse_case]
        
    # Caso de 100 elementos
    better_case, average_case, worse_case = createListCase(100, 1000)
    data_100elements = [better_case, average_case, worse_case]
        
    # Caso de 1000 elementos
    better_case, average_case, worse_case = createListCase(1000, 10000)
    data_1000elements = [better_case, average_case, worse_case]
    
    endProgram = False
    while not endProgram:
        print("//MEDIDOR DE ALGORITMOS//\n"
              "a) Iniciar pruebas generales\n"
              "b) Iniciar pruebas individuales\n"
              "c) Cerrar")
        option_selected = input("[INGRESE UNA OPCION]")
               
        if option_selected in 'a':
            generalTest(data_10elements, data_100elements, data_1000elements)
        elif option_selected in 'b':
            individualTest(data_10elements, data_100elements, data_1000elements)
        elif option_selected in 'c':
            endProgram = True
        else:
            print(warning  + "Ingrese un caracter valido")
        os.system("cls")
            
      
        
        
        
        
    