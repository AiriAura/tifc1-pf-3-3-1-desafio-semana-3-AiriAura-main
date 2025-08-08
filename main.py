def main():
    print("Desafio semana 3")

def countvowels(palabra):
    vocales = "aeiou"
    cant_vocales = 0
    for letra in palabra.lower():
        if letra in vocales:
            cant_vocales += 1
    return cant_vocales






if __name__ == "__main__":
    main()
