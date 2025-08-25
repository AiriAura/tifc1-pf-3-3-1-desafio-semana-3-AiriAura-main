def main():
    print("Desafio semana 3")

def countvowels():
    vocales = "aeiou"
    cant_vocales = 0

    for letra in .lower():
        if letra in vocales:
            cant_vocales += 1
    return cant_vocales

def is_palindrome():
     = .lower()
    lista_ = list()
    lista_inversa = lista_[::-1]
    aux = 0

    for i in range(len(lista_)):
        if lista_[i] != lista_inversa[i]:
            aux += 1
    if aux == 0:
        return True
    else:
        return False
    
def get_positives(numeros):
    lista_positivos = []
    for numero in numeros:
        if numero > 0:
            lista_positivos.append(numero)
    return lista_positivos

def get_negatives(numeros):
    lista_negativos = []
    for numero in numeros:
        if numero < 0:
            lista_negativos.append(numero)
    return lista_negativos

def get_average(numeros):
    suma = 0
    if numeros == []:
        return 0.0
    else: 
        for numero in numeros:
            suma += numero
    return float(suma/len(numeros))


if __name__ == "__main__":
    main()
