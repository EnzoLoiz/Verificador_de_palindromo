
def checando_palindromo(entrada_principal, entrada_invertida):
    if entrada_principal == entrada_invertida:
        resultado= print(f"{Entrada_1} é um palíndromo")
    else:
        resultado= print(f"{Entrada_1} não é um palíndromo")

while True:
    Entrada_1 = input("Digite a palavra para checar se é palindromo: ")
    Entrada_1_sem_espaco = Entrada_1.replace(" ","")
    Entrada_1_final= Entrada_1_sem_espaco.upper()
    
    Entrada_invertida= Entrada_1_final[::-1]

    checando_palindromo(Entrada_1_final, Entrada_invertida)
    