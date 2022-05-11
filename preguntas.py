"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    with open("data.csv",'r') as x:
        data = csv.reader(x,delimiter = "\t")
        columns = list (data)

    suma=0

    for num in columns:
        suma += int(num[1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data = file.readlines()

    data = [row[0] for row in data]

    result = dict()

    for letra in data:
        if letra in result.keys():
            result[letra] = result[letra] + 1
        else:
            result[letra] = 1
    tuplas = [(key, valor) for key, valor in result.items()]
    tuplas = sorted(tuplas, key=itemgetter(0), reverse=False)
    
    return tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    import csv
    from collections import Counter
    with open("data.csv",newline='') as t:
        data = csv.reader(t,delimiter ="\t")
        columns =list(data)
    lista = list()
    for i in columns:
        a= i[:2]
        lista.append(a)
    sumatoria= {}
    for row in lista:
        key = row[0]
        value = int(row[1])
        if key in sumatoria:
            sumatoria[key] += value
        else:
            sumatoria[key] = value

    diccionario = dict(sorted(sumatoria.items(), key=lambda item: item[0]))

    tuplas = list(diccionario.items())
 
    return tuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    import csv
    from collections import Counter
    with open("data.csv",newline='') as t:
        data = csv.reader(t,delimiter ="\t")
        columns =list(data)
    lista = list()
    for i in columns:
        a= i[2]
        lista.append(a)
    lista1 = list()
    for x in lista:
        c=x[5:7]
        lista1.append(c)
    frecuencia={}
    for n in lista1:
        if n in frecuencia:
            frecuencia[n] += 1
        else: 
            frecuencia[n] =1

    diccionario = dict(sorted(frecuencia.items(), key=lambda item: item[0]))

    tuplas = list(diccionario.items())
    
    return tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    import csv
    from collections import Counter
    from operator import itemgetter
    with open("data.csv",newline='') as t:
        data = csv.reader(t,delimiter ="\t")
        columns =list(data)
    lista = [row[0] for row in columns]
    lista1 = [int(fila[1]) for fila in columns]
    lista2 = list(zip(lista,lista1))
    diccionario= {}
    for row in lista2:
        key = row[0]
        valor = []
        valor1 = row[1]
        if key in diccionario:
            diccionario[key].append(valor1)
        else:
            diccionario[key]=valor
            diccionario[key].append(valor1)
    diccionario = [(key,max(valor),min(valor)) for key,valor in diccionario.items()]
    diccionario = sorted(diccionario,key = itemgetter(0), reverse = False)
    
    return diccionario


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    import csv
    from operator import itemgetter
    with open ("data.csv","r") as file:
        data = file.readlines()
    data1= [row[:-1] for row in data]
    data2 = [str(row).split("\t")[-1] for row in data1]
    data4 = []
    data5=[]
    for row in data2:
        a= row.split(",")
        data4.extend(a)
    for row in data4:
        b= row.split(":")
        data5.extend(b)
    x= data5[0::2]
    y = data5[1::2]
    xy = zip(x,y)
    diccionario= {}
    for row in xy:
        key = row[0]
        valor = []
        valor1 = int(row[1])
        if key in diccionario:
            diccionario[key].append(valor1)
        else:
            diccionario[key]=valor
            diccionario[key].append(valor1)
    diccionario = [(key,min(valor),max(valor)) for key,valor in diccionario.items()]
    diccionario = sorted(diccionario,key = itemgetter(0), reverse = False)
    
    return diccionario


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    import csv
    from collections import Counter
    from operator import itemgetter
    with open("data.csv",newline='') as t:
        data = csv.reader(t,delimiter ="\t")
        columns =list(data)
    lista = [row[0] for row in columns]
    lista1 = [int(fila[1]) for fila in columns]
    lista2 = list(zip(lista,lista1))
    diccionario = {}
    for row in lista2:
        key = row[1]
        valor = []
        valor1 = row[0]
        if key in diccionario:
            diccionario[key].append(valor1)
        else:
            diccionario[key]=valor
            diccionario[key].append(valor1)
    diccionario1 = dict(sorted(diccionario.items(), key=lambda item: item[0]))

    tuplas = list(diccionario1.items())

    return tuplas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    import csv
    from collections import Counter
    from operator import itemgetter
    with open("data.csv",newline='') as t:
        data = csv.reader(t,delimiter ="\t")
        columns =list(data)
    lista = [row[0] for row in columns]
    lista1 = [int(fila[1]) for fila in columns]
    lista2 = set(list(zip(lista,lista1)))
    lista3 = sorted(lista2, key = lambda ord : ord[0])
    diccionario = {}
    for row in lista3:
        key = row[1]
        valor = []
        valor1 = row[0]
        if key in diccionario:
            if valor1 in valor:
                next
            else:
                diccionario[key].append(valor1)
        else:
            diccionario[key]=valor
            diccionario[key].append(valor1)

    diccionario1 = dict(sorted(diccionario.items(), key=lambda item: item[0]))

    tuplas = list(diccionario1.items())
    
    return tuplas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open ("data.csv","r") as file:
        data = file.readlines()
    data1= [row[:-1] for row in data]
    data2 = [str(row).split("\t")[-1] for row in data1]
    data3 = []
    data4=[]
    for row in data2:
        a= row.split(",")
        data3.extend(a)
    for row in data3:
        b= row.split(":")
        data4.extend(b)
    x= data4[0::2]
    y = data4[1::2]
    xy = zip(x,y)
    diccionario = {}
    for row in xy:
        key = row[0]
        if key in diccionario:
            diccionario[key] += 1
        else:
            diccionario[key] = 1
    diccionario1 = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    
    return diccionario1


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    import csv
    from operator import itemgetter
    with open ("data.csv","r") as file:
        data = file.readlines()
    data1= [row for row in data]
    data2 = [str(row).split("\t")[-1].split(",") for row in data1]
    data3 = [str(row).split("\t")[-2].split(",") for row in data1]
    data4 = [len(row) for row in data2]
    data5 = [row[0] for row in data]
    data6 = [len(row) for row in data3]
    lista=zip(data5,data6,data4)
    
    return list(lista)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    import csv
    from operator import itemgetter
    with open ("data.csv","r") as file:
        data = file.readlines()
    data1= [row for row in data]
    data2 = [str(row).split("\t")[-2] for row in data1]
    data3 = [row[2] for row in data]
    data4 =[]
    for row1,row2 in zip(data2,data3):
        a = str(row1+","+row2)
        data4.append(a.split(","))

    data5 = [str(row).split(",") for row in data4]
    data6 =[]
    for row in data5:
        for value in row[:-1]:
            a= list(value + "," + row[-1])
            data6.append(a)
    data7 =[row[2] for row in data6]
    data8 =[int(row[7]) for row in data6]
    data9 = zip(data7,data8)
    sumatoria= {}
    for row in data9:
        key = row[0]
        value = int(row[1])
        if key in sumatoria:
            sumatoria[key] += value
        else:
            sumatoria[key] = value

    diccionario = dict(sorted(sumatoria.items(), key=lambda item: item[0]))
    
    return diccionario


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    with open ("data.csv","r") as file:
        data = file.readlines()

    data = [row.replace('\n','')for row in data]
    data1 = [(row.split('\t')[0],(row.split('\t')[-1])) for row in data]
    data2 = []
    for i in data1:
        data3 = i[1].split(",")
        for h in data3:
            data4 = int(h.split(":")[1])
            data5= (i[0], data4)
            data2.append(data5)
    diccionario = {}
    for row in data2:
        key = row[0]
        valor = int(row[1])
        if key in diccionario:
            diccionario[key] += valor
        else:
            diccionario[key] = valor

    diccionario1 = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    
    return diccionario1
