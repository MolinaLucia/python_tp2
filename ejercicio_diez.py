nombres=''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1=[81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 =[30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


# Con el metodo replace reemplazo las comas y los espacios en blanco por vacio
nombres=nombres.replace(",","").replace("'","") 
# Genero una lista de nombres
nombres=nombres.split() 

def generar_estructura():
    # Genero una lista sumando los elementos de notas_1 + notas_2
    agrupar_notas=list(map(lambda nota1,nota2: (nota1+nota2), notas_1,notas_2)) 

    # Genero una estructura de tipo diccionario comprimiendo (con zip) la lista de nombres y la lista de agrupar_notas
    # El diccionario tendra nombres(clave) y notas(valor)
    dicci={}
    for identidad, nota in zip(nombres, agrupar_notas):
        dicci[identidad] = nota  
    return dicci


def calcular_promedio_estudiante():
    # Utilizo lambda para generar el calulo del promedio por estudiante
    # La funcion map devuelve un iterador que contiene los resultados, iterando sobre los elementos del diccionario.
    promedios=map(lambda x:(f"El promedio de {x} es: {dicci[x]/2}"), dicci)
    
    # Como promedios es de tipo map --> iterador que contiene los resultados tengo que hacer un for para imprimir el contenido
    for prom in promedios:
        print(prom)   
        

def promedio_general():
    # Convierto en integer el 'valor' del diccionario y lo divido por dos (porque hay dos notas por estudiante) para sacar el primedio por estudiante 
    # Dicho resultado lo guardo en una variable promedio_estudiante de tipo iterable(map)
    promedio_estudiante = map(lambda x: int(dicci[x]/2), dicci)
    
    #Como promedio_estudiante es de tipo map,iterable,sumo cada promedio de dicha variable y lo divido por el total de elementos
    promedio_general = sum(promedio_estudiante)/len(dicci)
    print(f'>> El promedio general del curso es {promedio_general}')

    
def maximo_promedio():
    # Con .items() nos permite obtener de forma par la clave y valor.
    # la funcion max() se usa para encontrar el valor maximo en un iterable,en este caso diccionario   
    maximo= max(dicci.items(), key=lambda x: x[1])
    print(f">> El mayor promedio lo obtuvo {maximo[0]} con {maximo[1]/2}")

        
def minimo_promedio():
    minimo= min(dicci.items(), key=lambda x: x[1])
    print(f">> El minimo promedio lo obtuvo {minimo[0]} con {minimo[1]/2}")
      
        
dicci=generar_estructura() 
calcular_promedio_estudiante() 
promedio_general()
maximo_promedio() 
minimo_promedio() 