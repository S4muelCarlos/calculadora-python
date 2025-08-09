import tkinter as tk

def somar():
    try:
        resultado = float(entrada.get()) + float(entrada2.get())
        label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

def subtrair():
    try:
        resultado = float(entrada.get()) - float(entrada2.get())
        label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

def multiplicar():
    try:
        resultado = float(entrada.get()) * float(entrada2.get())
        label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

def dividir():
    try:
        num1 = float(entrada.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            label_resultado.config(text="Erro! Divisão por zero.")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

def potenciação():
    try:
        resultado = float(entrada.get()) ** float(entrada2.get())
        label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

def dividir_exata():
    try:
        num1 = float(entrada.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            label_resultado.config(text="Erro! Divisão por zero.")
        else:
            resultado = num1 // num2
            label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Tamanho da janela
root.geometry("300x400")

# Entrada do primeiro número
label_entrada = tk.Label(root, text="Digite o primeiro número:")
label_entrada.pack()

entrada = tk.Entry(root)
entrada.pack()

# Entrada do segundo número
label_entrada2 = tk.Label(root, text="Digite o segundo número:")
label_entrada2.pack()

entrada2 = tk.Entry(root)
entrada2.pack()

# Botões para as operações
button_soma = tk.Button(root, text="Soma", width=10, command=somar)
button_soma.pack(pady=5)

button_subtrair = tk.Button(root, text="Subtração", width=10, command=subtrair)
button_subtrair.pack(pady=5)

button_multiplicar = tk.Button(root, text="Multiplicação", width=10, command=multiplicar)
button_multiplicar.pack(pady=5)

button_dividir = tk.Button(root, text="Divisão", width=10, command=dividir)
button_dividir.pack(pady=5)

button_potenciação = tk.Button(root, text="Potenciação", width=10, command=potenciação)
button_potenciação.pack(pady=5)

button_dividir_exata = tk.Button(root, text="Divisão Exata", width=10, command=dividir_exata)
button_dividir_exata.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack(pady=20)

# Rodar a interface
root.mainloop()