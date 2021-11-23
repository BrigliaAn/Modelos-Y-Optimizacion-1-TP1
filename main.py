import itertools


def cargar_problema(archivo):
    incompatibilidades = {}
    tiempo_lavado = {}
    with open(archivo) as f:
        line = f.readline()
        while line:
            linea = line.split()
            if len(linea) > 0:
                if(linea[0] == 'p'):
                    cant_prendas = linea[2]
                    cant_incompatibilidades = linea[3]
                if(linea[0] == 'e'):
                    if(int(linea[1]) in incompatibilidades.keys()):
                        incompatibilidades[int(linea[1])].append(int(linea[2]))
                    else:
                        incompatibilidades[int(linea[1])] = [int(linea[2])]
                    if(int(linea[2]) in incompatibilidades.keys()):
                        incompatibilidades[int(linea[2])].append(int(linea[1]))
                    else:
                        incompatibilidades[int(linea[2])] = [int(linea[1])]

                if(linea[0] == 'n'):
                    if(int(linea[2]) in tiempo_lavado.keys()):
                        tiempo_lavado[int(linea[2])].append(int(linea[1]))
                    else:
                        tiempo_lavado[int(linea[2])] = [int(linea[1])]

            line = f.readline()
    return (cant_prendas, cant_incompatibilidades, incompatibilidades, tiempo_lavado)


def nuevo_lavado(nro_lavado, lavados, prenda):
    nro_lavado = len(lavados.keys()) + 1
    lavados[nro_lavado] = [prenda]


def verificar_si_es_compatible_en_lavado(prenda, nro_lavado, lavados, incompatibilidades):
    prendas_incompatibles = incompatibilidades.get(prenda)
    if (prendas_incompatibles):
        for prenda_en_lavado in lavados.get(nro_lavado):
            if prenda_en_lavado in prendas_incompatibles:
                return False
        return True
    else:
        return True


def verificar_si_es_compatible(prenda, prendas, incompatibilidades):
    prendas_incompatibles = incompatibilidades.get(prenda)
    if (prendas_incompatibles):
        for p in prendas:
            if p in prendas_incompatibles:
                return False
        return True
    else:
        return True


def agregar_prenda_en_lavado(nro_lavado, prenda, lavados):
    lavados[nro_lavado].append(prenda)


def imprimir_resultado(lavados):
    resultado = {}
    for k in lavados.keys():
        prendas = lavados.get(k)
        for prenda in prendas:
            if not resultado.get(prenda):
                resultado[prenda] = k
    return resultado


def flat_list_diccionario(dict):
    for k in dict.keys():
        flat_list = []
        for sublist in dict.get(k):
            if(isinstance(sublist, int)):
                flat_list.append(sublist)
            else:
                for item in sublist:
                    flat_list.append(item)
        dict[k] = flat_list
    return dict


def main():
    (cant_prendas, cant_incompatibilidades, incompatibilidades,
     tiempo_lavado) = cargar_problema("problema.txt")
    nro_lavado = 1
    lavados_compatibles_sin_tiempo = {}
    lavados_final = {}
    for prenda in range(1, int(cant_prendas)+1):
        nro_lavado = 1
        prenda_agregada = False
        if(nro_lavado in lavados_compatibles_sin_tiempo.keys()):
            while(nro_lavado < len(lavados_compatibles_sin_tiempo.keys())+1 and prenda_agregada == False):
                es_compatible = verificar_si_es_compatible_en_lavado(
                    prenda, nro_lavado, lavados_compatibles_sin_tiempo, incompatibilidades)
                if (es_compatible):
                    agregar_prenda_en_lavado(
                        nro_lavado, prenda, lavados_compatibles_sin_tiempo)
                    prenda_agregada = True
                else:
                    nro_lavado += 1
            if(prenda_agregada == False):
                nuevo_lavado(
                    nro_lavado, lavados_compatibles_sin_tiempo, prenda)
        else:
            nuevo_lavado(nro_lavado, lavados_compatibles_sin_tiempo, prenda)
    not_interseccion_final = []
    for lavado_compatible in lavados_compatibles_sin_tiempo.keys():
        prendas_compatibles = lavados_compatibles_sin_tiempo.get(
            lavado_compatible)
        for t in tiempo_lavado:
            prendas_igual_tiempo = tiempo_lavado.get(t)
            interseccion = list(
                set(prendas_compatibles).intersection(prendas_igual_tiempo))
            not_interseccion = list(
                set(prendas_compatibles) - set(prendas_igual_tiempo))
            if(interseccion):
                if lavado_compatible in lavados_final.keys():
                    lavados_final[lavado_compatible].append(interseccion)
                else:
                    lavados_final[lavado_compatible] = interseccion
            if(not_interseccion):
                for elem in not_interseccion:
                    if elem not in not_interseccion_final:
                        not_interseccion_final.append(elem)
    lavados_final = flat_list_diccionario(lavados_final)
    for elemento in not_interseccion_final:
        for n_lavado in lavados_final.keys():
            prendas = lavados_final.get(n_lavado)
            es_compatible = verificar_si_es_compatible(
                elemento, prendas, incompatibilidades)
            if(es_compatible):
                agregar_prenda_en_lavado(n_lavado, elemento, lavados_final)
                prenda_agregada = True
            else:
                prenda_agregada = False
        if(prenda_agregada == False):
            nro = len(lavados_final)
            nuevo_lavado(nro, lavados_final, elemento)
    print(lavados_compatibles_sin_tiempo)
    print(tiempo_lavado)
    print(lavados_final)
    resultado = imprimir_resultado(lavados_final)
    with open('resultado.txt', 'a') as f:
        for x in resultado:
            print(str(x) + ' ' + str(resultado.get(x)), file=f)


def main2():
    (cant_prendas, cant_incompatibilidades, incompatibilidades,
     tiempo_lavado) = cargar_problema("problema.txt")
    nro_lavado = 1
    lavados = {}
    for prenda in range(1, int(cant_prendas)+1):
        nro_lavado = 1
        prenda_agregada = False
        if(nro_lavado in lavados.keys()):
            while(nro_lavado < len(lavados.keys())+1 and prenda_agregada == False):
                es_compatible = verificar_si_es_compatible_en_lavado(
                    prenda, nro_lavado, lavados, incompatibilidades)
                if (es_compatible):
                    agregar_prenda_en_lavado(nro_lavado, prenda, lavados)
                    prenda_agregada = True
                else:
                    nro_lavado += 1
            if(prenda_agregada == False):
                nuevo_lavado(nro_lavado, lavados, prenda)
        else:
            nuevo_lavado(nro_lavado, lavados, prenda)

    print(lavados)
    print(tiempo_lavado)
    resultado = imprimir_resultado(lavados)
    with open('resultado.txt', 'a') as f:
        for x in resultado:
            print(str(x) + ' ' + str(resultado.get(x)), file=f)


main()
