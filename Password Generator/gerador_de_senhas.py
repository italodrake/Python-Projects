import secrets
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha(tamanho, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase  # Letras maiúsculas
    if usar_minusculas:
        caracteres += string.ascii_lowercase  # Letras minúsculas
    if usar_numeros:
        caracteres += string.digits  # Números
    if usar_simbolos:
        caracteres += string.punctuation  # Símbolos

    if not caracteres:
        raise ValueError("Ao menos um tipo de caractere deve ser selecionado para a senha.")

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_senhas_gui():
    try:
        quantidade_senhas = int(entry_quantidade_senhas.get())
        quantidade_caracteres = int(entry_quantidade_caracteres.get())

        if quantidade_senhas <= 0 or quantidade_caracteres <= 0:
            raise ValueError("Por favor, insira números maiores que 0.")
        
        # Gerar as senhas
        senhas_geradas = ""
        for _ in range(quantidade_senhas):
            senha = gerar_senha(quantidade_caracteres)
            senhas_geradas += senha + "\n"

        # Exibir as senhas na interface
        text_senhas.delete(1.0, tk.END)  # Limpar o texto antes de adicionar novas senhas
        text_senhas.insert(tk.END, senhas_geradas)
    
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("500x400")  # Tamanho da janela
root.config(bg="#f0f0f0")  # Cor de fundo

# Configuração dos componentes com cores e fontes personalizadas
label_quantidade_senhas = tk.Label(root, text="Quantidade de senhas:", font=("Helvetica", 12), bg="#f0f0f0")
label_quantidade_senhas.pack(pady=10)

entry_quantidade_senhas = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="solid", width=30)
entry_quantidade_senhas.pack(pady=5)

label_quantidade_caracteres = tk.Label(root, text="Quantidade de caracteres por senha:", font=("Helvetica", 12), bg="#f0f0f0")
label_quantidade_caracteres.pack(pady=10)

entry_quantidade_caracteres = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="solid", width=30)
entry_quantidade_caracteres.pack(pady=5)

botao_gerar = tk.Button(root, text="Gerar Senhas", command=gerar_senhas_gui, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", bd=0, relief="solid", width=20)
botao_gerar.pack(pady=20)

text_senhas = tk.Text(root, height=10, width=40, font=("Helvetica", 12), bd=2, relief="solid", wrap=tk.WORD)
text_senhas.pack(pady=10)

# Rodar a interface
root.mainloop()
