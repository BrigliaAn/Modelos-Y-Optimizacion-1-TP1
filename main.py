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
                if(linea[0] == 'n'):
                    tiempo_lavado[linea[1]] = linea[2]
            line = f.readline()
    return (cant_prendas, cant_incompatibilidades, incompatibilidades, tiempo_lavado)


def nuevo_lavado(nro_lavado, lavados, prenda):
    nro_lavado = len(lavados.keys()) + 1
    lavados[nro_lavado] = [prenda]


def verificar_si_es_compatible(prenda, nro_lavado, lavados, incompatibilidades):
    prendas_incompatibles = incompatibilidades.get(prenda)
    if (prendas_incompatibles):
        for prenda_en_lavado in lavados.get(nro_lavado):
            if prenda_en_lavado in prendas_incompatibles:
                return False
        return True
    else:
        return True


def agregar_prenda_en_lavado(nro_lavado, prenda, lavados):
    lavados[nro_lavado].append(prenda)


def main():
    (cant_prendas, cant_incompatibilidades, incompatibilidades,
     tiempo_lavado) = cargar_problema("problema.txt")
    nro_lavado = 1
    lavados = {}
    for prenda in range(1, int(cant_prendas)+1):
        nro_lavado = 1
        prenda_agregada = False
        if(nro_lavado in lavados.keys()):
            while(nro_lavado < len(lavados.keys())+1 and prenda_agregada == False):
                es_compatible = verificar_si_es_compatible(
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


main()
