import tkinter as tk
from tkinter import ttk

def checando_palindromo(entrada_principal, entrada_invertida):
    if entrada_principal == entrada_invertida:
        return True
    else:
        return False


def verificar_palindromo():
    entrada = entrada_palavra.get()
    Entrada_sem_espaco = entrada.replace(" ","")
    Entrada_final= Entrada_sem_espaco.upper()

    entrada_invertida = Entrada_final[::-1]
    if checando_palindromo(Entrada_final, entrada_invertida):
        label_resultado_final.config(text=f"{entrada} é um palíndromo")
    else:
        label_resultado_final.config(text=f"{entrada} não é um palíndromo")

janela= tk.Tk()
janela.title("Verificador de Palíndromo")
janela.geometry("300x200")

label_instrucao_usuario=tk.Label(janela, text="digite aqui a palavra que será verificada: ")
label_instrucao_usuario.pack(pady=5)


entrada_palavra = tk.Entry(janela)
entrada_palavra.pack(pady=5)

botao_de_verificar=tk.Button(janela,text="Verificar palavra", command=verificar_palindromo)
botao_de_verificar.pack(pady=5)

label_resultado_final=tk.Label(janela, text='')
label_resultado_final.pack(pady=5)

janela.mainloop()