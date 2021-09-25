def main():
    incompatibilidades = {}
    tiempo_lavado = {}
    nro_lavado = 1
    lavados = {}
    with open('problema.txt') as f:
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
    for prenda in range(1, int(cant_prendas)+1):
        nro_lavado = 1
        if(nro_lavado in lavados.keys()):
            prenda_agregada = False
            prendas_incompatibles = incompatibilidades.get(prenda)
            if (prendas_incompatibles):
                for prenda_en_lavado in lavados.get(nro_lavado):
                    if prenda_en_lavado in prendas_incompatibles:
                        nro_lavado = len(lavados.keys()) + 1
                        lavados[nro_lavado] = [prenda]
                        prenda_agregada = True
                        break
                if(prenda_agregada == False):
                    lavados[nro_lavado].append([prenda])
            else:
                lavados[nro_lavado].append([prenda])
        else:
            lavados[nro_lavado] = [prenda]

    print(lavados)


main()
