from random import randint
from random import shuffle
from models.data import dataElement, case
from models.pdf import PDF
from pathlib import Path
from shutil import copy
import sys
import os
import models.methods as methods 

# Aumentar limite de recursion
sys.setrecursionlimit(3000)

# Variables globales
file_name = "reporte_metodos"
pathUser = Path.home()
warning = "[*] WARNING: "
output_count = "[TIEMPO] => "
results_title = "Resultados:"
error = "[!] ERROR: "

'''FUNCIONES PARA CREAR PDFs'''
def moveFile(option):
    dirToMove = ""
    if option == 'a':
        dirToMove = 'Desktop'
    else:
        dirToMove = 'Documents'
    
    try:
        copy(f"{os.getcwd()}\\pdf\\{file_name}.pdf" ,f"{pathUser}\\{dirToMove}\\{file_name}.pdf")
        print(">> ARCHIVO GUARDADO CORRACTAMENTE")
        enterToContinue()
        
    except Exception as e:
        print(error + str(e))
        print(f"Archivo igual existe en: {pathUser}/Documents/EDD2PROYECTO/pdf")
        enterToContinue() 
    
def saveIn():
    print("\nDesea salvar en:\n"
          "a) Escritorio\n"
          "b) Documentos\n"
          "c) Dejar guardado en C:/Users/User/Documents/EDD2PROYECTO/pdf")
    print("---------------------------------------------------------")
    option = input("[INGRESE UNA OPCION] => ")
    
    if option == 'a' or option == 'b': 
        moveFile(option)
     
def captureNameFile():
    name = input(">> Ingrese el nombre del archivo [ENTER PARA DEFAULT] => ")
    if not name == "":
        file_name = name
    
def makeReportPDFs(list_methods, data_10elements, data_100elements, data_1000elements):
    captureNameFile()
    
    try:
        pdf = PDF()
        pdf.makePDF(list_methods, file_name, [data_10elements, data_100elements, data_1000elements]) 
        print(">> PDF CREADO!!!")
        saveIn()
        
    except Exception as e:
        print(error + str(e))
        enterToContinue()

'''FUNCIONES PARA APLICAR TEST'''
def applyTest(results_method, method_function, data_10elements, data_100elements, data_1000elements):
   
    # Guardar resultados de lista de 10
    results_method.getData10().setAllAttributes(
    method_function(data_10elements[0]), 
    method_function(data_10elements[1]),
    method_function(data_10elements[2]))
        
    #Guardar resultados de lista de 100
    results_method.getData100().setAllAttributes(
    method_function(data_100elements[0]), 
    method_function(data_100elements[1]),
    method_function(data_100elements[2]))
    
    # Guardar resultados de lista de 1000
    results_method.getData1000().setAllAttributes(
    method_function(data_1000elements[0]), 
    method_function(data_1000elements[1]),
    method_function(data_1000elements[2]))
    
'''FUNCIONES PARA MOSTRAR TESTS'''
def printResults10Elememts(results_method):
    print(results_title + 
        "\n>> Lista de 10 elementos:\n" 
        + output_count + f"Mejor caso {results_method.getData10().getBetterCase()}\n"       
        + output_count + f"Caso promedio {results_method.getData10().getAverageCase()}\n"
        + output_count + f"Peor caso {results_method.getData10().getWorseCase()}\n"
        + "---------------------------------------------------------")

def printResults100Elememts(results_method):
    print(results_title + 
        "\n>> Lista de 100 elementos:\n" 
        + output_count + f"Mejor caso {results_method.getData100().getBetterCase()}\n"       
        + output_count + f"Caso promedio {results_method.getData100().getAverageCase()}\n"
        + output_count + f"Peor caso {results_method.getData100().getWorseCase()}\n"
        + "---------------------------------------------------------")

def printResults1000Elememts(results_method):
    print(results_title + 
        "\n>> Lista de 1000 elementos:\n" 
        + output_count + f"Mejor caso {results_method.getData1000().getBetterCase()}\n"       
        + output_count + f"Caso promedio {results_method.getData1000().getAverageCase()}\n"
        + output_count + f"Peor caso {results_method.getData1000().getWorseCase()}\n"
        + "---------------------------------------------------------")
    
def showIndividualResults(results_method):
    print(f"\n<{results_method.getName()}>")
    
    printResults10Elememts(results_method)
    printResults100Elememts(results_method) 
    printResults1000Elememts(results_method)            
        
'''FUNCIONES PARA EJECUTAR TEST'''
def testMethod(results_method, function, name ,data_10elements, data_100elements, data_1000elements):
    applyTest(results_method, function, data_10elements, data_100elements, data_1000elements)
    results_method.setName(name)
    showIndividualResults(results_method)

def generalTest(data_10elements, data_100elements, data_1000elements):
    
    bubble_method =  dataElement()
    testMethod(bubble_method, methods.bubble_sort, "Bubble sort", 
        data_10elements, data_100elements, data_1000elements)
    
    insertion_method = dataElement()
    testMethod(insertion_method, methods.insertion_sort, "Insertion sort", 
        data_10elements, data_100elements, data_1000elements)

    quicksort_method = dataElement()
    testMethod(quicksort_method, methods.quicksort, "Quick sort", 
        data_10elements, data_100elements, data_1000elements)  
    
    selection_method = dataElement()
    testMethod(selection_method, methods.selection_sort, "Selection sort", 
        data_10elements, data_100elements, data_1000elements)
        
    shellShort = dataElement()
    testMethod(shellShort, methods.shellShort, "Shellshort", 
        data_10elements, data_100elements, data_1000elements)
        
    shakersort_method = dataElement() 
    testMethod(shakersort_method, methods.shakerSort, "Shaker sort", 
                      data_10elements, data_100elements, data_1000elements)

    return [bubble_method, insertion_method, quicksort_method, selection_method, shellShort, shakersort_method] 
    
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

def createDataSets():
     # Caso de 10 elementos
    better_case, average_case, worse_case = createListCase(10,100)
    data_10elements = [better_case, average_case, worse_case]
        
    # Caso de 100 elementos
    better_case, average_case, worse_case = createListCase(100, 1000)
    data_100elements = [better_case, average_case, worse_case]
        
    # Caso de 1000 elementos
    better_case, average_case, worse_case = createListCase(1000, 10000)
    data_1000elements = [better_case, average_case, worse_case]

    return data_10elements, data_100elements, data_1000elements

if __name__ == "__main__":
    
    data_10elements, data_100elements, data_1000elements = createDataSets()
    
    endProgram = False
    while not endProgram:
        print("//MEDIDOR DE ALGORITMOS//\n"
              "a) Iniciar pruebas individuales\n"
              "q) Cerrar\n"
              + "---------------------------------------------------------")
        option_selected = input("[INGRESE UNA OPCION] => ")
               
        if option_selected in 'a':
            list_methods = generalTest(data_10elements, data_100elements, data_1000elements)
            enterToContinue()
            data_10elements, data_100elements, data_1000elements = createDataSets()
            makeReportPDFs(list_methods, data_10elements, data_100elements, data_1000elements)
            
        elif option_selected in 'q':
            endProgram = True
        os.system("cls")
        
            
      
        
        
        
        
    