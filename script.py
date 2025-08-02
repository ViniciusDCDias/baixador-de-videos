import tkinter as tk
from tkinter import Entry, Button, messagebox
import yt_dlp

def baixar_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return
    
    try:
        ydl_opts = {"format": "best", "outtmpl": "./downloads/%(title)s.%(ext)s"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")

# Criando a janela principal
janela = tk.Tk()
janela.title("YouTube Downloader")
janela.geometry("500x300")
janela.configure(bg="#b3b3b3")  # Fundo cinza

# Campo de texto "Insira o link do vídeo:"
tk.Label(janela, text="Insira o link do vídeo:", fg="black", background="#b3b3b3",justify="center").pack(pady=10)

# Campo de entrada arredondado
url_entry = Entry(janela, font=("Arial", 14), bd=5, relief="ridge", width=30, justify="center", textvariable="Insira a URL")
url_entry.place(x=100, y=100, height=40)

# Botão vermelho "PRONTO"
botao = Button(janela, text="PRONTO", font=("Arial", 14), bg="red", fg="black", bd=3, relief="ridge", command=baixar_video)
botao.place(x=200, y=160, width=100, height=40)

# Inicia a interface gráfica
janela.mainloop()
