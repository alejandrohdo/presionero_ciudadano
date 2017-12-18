# -*- coding: utf-8 -*-
def v_valores(valores):
    estado = True
    for x in valores:
        if int(x) >= 0 and int(x) <= 10:
            pass
        else:
            estado = False
    return estado

def v_poligonos(poligonos):
    estado = True
    for x in poligonos:
        if len(x) >= 3 and len(x) <= 12:
            pass
        else:
            estado = False
    return estado
def comprobar_caso(x, y, valores):
    mensaje_salida = False
    mensaje = ''
    i = 0
    j = len(valores) - 1
    # aplicando Teorema curva de Jordan, x,y --> RxR, en un plano 
    for i in range(len(valores)):
        if (valores[i][1] < y and valores[j][1] >= y) or (valores[j][1] < y and valores[i][1] >= y):
            if valores[i][0] + (y - valores[i][1]) / (valores[j][1] - valores[i][1]) * (valores[j][0] - valores[i][0]) < x:
                mensaje_salida = not mensaje_salida
        j = i
    if mensaje_salida:
        mensaje = 'Presionero'
    else:
        mensaje = 'Ciudadano'
    return mensaje

if __name__ == '__main__':
    texto = 'archivo.txt'
    archivo = open(texto)
    if archivo is not None:
        poligonos, puntos, valores_poligonos, valores_puntos = [], [], [], []
        with archivo as f:
            for line in f:
                vertices, punto = line.split(" | ")
                poligonos.append([tuple(int(c) for c in vertice.split())
                                  for vertice in vertices.split(", ")])
                puntos.append(tuple(int(c) for c in punto.split()))
                
                for vertices1 in vertices.split(", "):
                    for c1 in vertices1.split():
                        valores_poligonos.append(c1)
                for ca in punto.split():
                    valores_puntos.append(ca)
        if v_valores(valores_poligonos) and v_valores(valores_puntos) and v_poligonos(poligonos):
            for i in range(len(poligonos)):
                x1, y1 = puntos[i]
                parametro = poligonos[i]
                print('imprimiendo: %s' % (i+1), 'soy=> %s' %
                      comprobar_caso(x1, y1, parametro))
        else:
            print('''Solo se permite valores de 0 a 10 y Nro de Cordenadas 
        		 de 3 a 12.., corrija las coordenadas del archivo..!''')
