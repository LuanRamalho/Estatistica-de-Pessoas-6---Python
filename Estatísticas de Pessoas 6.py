import tkinter as tk
from tkinter import ttk

# Função para calcular estatísticas
def calcular_estatisticas():
    try:
        # Pegando os valores dos campos de entrada
        branca = int(entry_branca.get() or 0)
        parda = int(entry_parda.get() or 0)
        preta = int(entry_preta.get() or 0)
        amarela = int(entry_amarela.get() or 0)
        indigena = int(entry_indigena.get() or 0)
        
        total_pessoas = branca + parda + preta + amarela + indigena

        # Calculando as porcentagens
        porcentagem_branca = (branca / total_pessoas) * 100 if total_pessoas else 0
        porcentagem_parda = (parda / total_pessoas) * 100 if total_pessoas else 0
        porcentagem_preta = (preta / total_pessoas) * 100 if total_pessoas else 0
        porcentagem_amarela = (amarela / total_pessoas) * 100 if total_pessoas else 0
        porcentagem_indigena = (indigena / total_pessoas) * 100 if total_pessoas else 0

        # Exibindo os resultados
        resultados_label.config(text=f"Total de pessoas pesquisadas: {total_pessoas}\n"
                                     f"Pessoas que se declaram brancas: {branca} ({porcentagem_branca:.2f}%)\n"
                                     f"Pessoas que se declaram pardas: {parda} ({porcentagem_parda:.2f}%)\n"
                                     f"Pessoas que se declaram pretas: {preta} ({porcentagem_preta:.2f}%)\n"
                                     f"Pessoas que se declaram amarelas: {amarela} ({porcentagem_amarela:.2f}%)\n"
                                     f"Pessoas que se declaram indígenas: {indigena} ({porcentagem_indigena:.2f}%)")
        
        # Atualizando as barras de progresso
        barra_branca['value'] = porcentagem_branca
        barra_parda['value'] = porcentagem_parda
        barra_preta['value'] = porcentagem_preta
        barra_amarela['value'] = porcentagem_amarela
        barra_indigena['value'] = porcentagem_indigena
    except ValueError:
        resultados_label.config(text="Por favor, insira valores válidos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Estatísticas de Cor/Raça")
janela.geometry("500x650")
janela.config(bg="#F0F8FF")

# Label principal
tk.Label(janela, text="Estatísticas de Cor/Raça", font=("Arial", 18, "bold"), bg="#F0F8FF", fg="#4682B4").pack(pady=15)

# Grupos de entrada
frame_entradas = tk.Frame(janela, bg="#F0F8FF")
frame_entradas.pack(pady=10)

# Função auxiliar para criar entradas de texto com estilo
def criar_entrada(rotulo_texto):
    frame = tk.Frame(frame_entradas, bg="#F0F8FF")
    frame.pack(fill="x", pady=5)
    rotulo = tk.Label(frame, text=rotulo_texto, bg="#F0F8FF", fg="#4682B4", font=("Arial", 12))
    rotulo.pack(side="left")
    entrada = tk.Entry(frame, font=("Arial", 12))
    entrada.pack(side="right", fill="x", expand=True)
    return entrada

# Criando entradas
entry_branca = criar_entrada("Pessoas que se consideram Brancas:")
entry_parda = criar_entrada("Pessoas que se consideram Pardas:")
entry_preta = criar_entrada("Pessoas que se consideram Pretas:")
entry_amarela = criar_entrada("Pessoas que se consideram Amarelas:")
entry_indigena = criar_entrada("Pessoas que se consideram Indígenas:")

# Botão para calcular estatísticas
calcular_btn = tk.Button(janela, text="Calcular Estatísticas", command=calcular_estatisticas, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
calcular_btn.pack(pady=15)

# Resultados e barras de progresso
resultados_label = tk.Label(janela, font=("Arial", 12), justify="left", bg="#F0F8FF", fg="#333333")
resultados_label.pack(pady=10)

# Função auxiliar para criar barras de progresso com estilo
def criar_barra(texto, cor_barra):
    frame = tk.Frame(janela, bg="#F0F8FF")
    frame.pack(fill="x", padx=20, pady=5)
    rotulo = tk.Label(frame, text=texto, bg="#F0F8FF", fg="#4682B4", font=("Arial", 12))
    rotulo.pack(side="left")
    barra = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
    barra.pack(side="right")
    # Aplicando uma cor específica para cada barra
    estilo = ttk.Style()
    estilo.configure("TProgressbar", troughcolor="white", background=cor_barra, thickness=15)
    return barra

# Criando barras de progresso com cores distintas
barra_branca = criar_barra("Branca:", "#87CEEB")
barra_parda = criar_barra("Parda:", "#FFD700")
barra_preta = criar_barra("Preta:", "#8B4513")
barra_amarela = criar_barra("Amarela:", "#FF6347")
barra_indigena = criar_barra("Indígena:", "#32CD32")

# Inicializar a janela
janela.mainloop()
