import random
import tkinter as tk
import customtkinter as ctk

def carregar_paises(continente):
    """
    Carrega os países do ficheiro correspondente ao continente escolhido.
    """
    ficheiro = f"{continente.lower()}.txt"  # Nome do ficheiro baseado no continente
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            paises = f.read().splitlines()
        return paises if paises else None
    except FileNotFoundError:
        return None

def sortear_pais(continente):
    """
    Sorteia aleatoriamente um país do continente escolhido.
    """
    paises = carregar_paises(continente)
    if paises:
        return random.choice(paises)
    return "Nenhum país disponível"

def validar_palpites(pais_correto, palpite):
    """
    Verifica se o palpite do utilizador está correto.
    """
    return palpite.strip().lower() == pais_correto.strip().lower()

def atualizar_tentativas(entry_tentativas):
    """
    Atualiza o número de tentativas falhadas.
    """
    try:
        tentativas = int(entry_tentativas.get())
    except ValueError:
        tentativas = 0
    entry_tentativas.delete(0, "end")
    entry_tentativas.insert(0, str(tentativas + 1))

def adicionar_pais(continente, pais):
    """
    Adiciona um novo país ao ficheiro correspondente ao continente.
    """
    ficheiro = f"{continente.lower()}.txt"
    with open(ficheiro, "a", encoding="utf-8") as f:
        f.write(f"{pais}\n")

def jogar():
    continente = entryContinente.get()
    pais_sorteado = sortear_pais(continente)
    entryPaisSorteado.delete(0, "end")
    entryPaisSorteado.insert(0, pais_sorteado)

def verificar_palpite():
    if validar_palpites(entryPaisSorteado.get(), entryPais.get()):
        lblResultado.configure(text="Acertaste!", fg="green")
    else:
        atualizar_tentativas(entryErradas)
        lblResultado.configure(text="Erraste!", fg="red")

def adicionar_novo_pais():
    adicionar_pais(entryContinente.get(), entryNovoPais.get())
    lblResultado.configure(text="País adicionado!", fg="blue")

# Interface gráfica com customtkinter
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Jogo dos Países")
app.geometry("400x400")

ctk.CTkLabel(app, text="Continente:").pack()
entryContinente = ctk.CTkEntry(app)
entryContinente.pack()

ctk.CTkLabel(app, text="País Sorteado:").pack()
entryPaisSorteado = ctk.CTkEntry(app)
entryPaisSorteado.pack()

btnSortear = ctk.CTkButton(app, text="Sortear País", command=jogar)
btnSortear.pack()

ctk.CTkLabel(app, text="Teu Palpite:").pack()
entryPais = ctk.CTkEntry(app)
entryPais.pack()

btnVerificar = ctk.CTkButton(app, text="Verificar", command=verificar_palpite)
btnVerificar.pack()

lblResultado = ctk.CTkLabel(app, text="")
lblResultado.pack()

ctk.CTkLabel(app, text="Tentativas Erradas:").pack()
entryErradas = ctk.CTkEntry(app)
entryErradas.insert(0, "0")
entryErradas.pack()

ctk.CTkLabel(app, text="Novo País:").pack()
entryNovoPais = ctk.CTkEntry(app)
entryNovoPais.pack()

btnAdicionar = ctk.CTkButton(app, text="Adicionar País", command=adicionar_novo_pais)
btnAdicionar.pack()

app.mainloop()
