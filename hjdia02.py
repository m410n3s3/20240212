import tkinter as tk
import random

# Contadores de bananas e upgrades
banana_contagem = {
    "amarela": 0,
    "verde": 0,
    "azul": 0,
    "vermelha": 0
}
upgrades = {
    "auto_click": False,
    "banana_rara": False,
    "duplicador": 0,
    "triplificador": 0
}

# Inicialização da velocidade do auto-clique (em milissegundos) e custo inicial
auto_click_speed = 1000
auto_click_custo = 50

# Função para gerar uma banana aleatória
def gerar_banana():
    chance = random.random()
    bananas_ganhas = 1
    bananas_ganhas *= 2 ** upgrades["duplicador"]  # Duplica com base no número de duplicadores
    bananas_ganhas *= 3 ** upgrades["triplificador"]  # Triplica com base no número de triplificadores

    if upgrades["banana_rara"]:
        if chance < 0.40:
            banana_contagem["amarela"] += bananas_ganhas
            resultado['text'] = "🍌 Banana Amarela"
        elif chance < 0.65:
            banana_contagem["verde"] += bananas_ganhas
            resultado['text'] = "🍏 Banana Verde"
        elif chance < 0.90:
            banana_contagem["azul"] += bananas_ganhas
            resultado['text'] = "🍌 Banana Azul"
        else:
            banana_contagem["vermelha"] += bananas_ganhas
            resultado['text'] = "🍓 Banana Vermelha"
    else:
        if chance < 0.50:
            banana_contagem["amarela"] += bananas_ganhas
            resultado['text'] = "🍌 Banana Amarela"
        elif chance < 0.80:
            banana_contagem["verde"] += bananas_ganhas
            resultado['text'] = "🍏 Banana Verde"
        elif chance < 0.95:
            banana_contagem["azul"] += bananas_ganhas
            resultado['text'] = "🍌 Banana Azul"
        else:
            banana_contagem["vermelha"] += bananas_ganhas
            resultado['text'] = "🍓 Banana Vermelha"
    
    # Atualizar placar
    atualizar_placar()

    # Se o auto-clique estiver ativado, gera uma nova banana após um tempo determinado
    if upgrades["auto_click"]:
        root.after(auto_click_speed, gerar_banana_auto)

# Função para o auto-clique gerar uma banana
def gerar_banana_auto():
    gerar_banana()

# Função para atualizar o placar
def atualizar_placar():
    placar_amarelo['text'] = f"Bananas Amarelas: {banana_contagem['amarela']}"
    placar_verde['text'] = f"Bananas Verdes: {banana_contagem['verde']}"
    placar_azul['text'] = f"Bananas Azuis: {banana_contagem['azul']}"
    placar_vermelho['text'] = f"Bananas Vermelhas: {banana_contagem['vermelha']}"

# Função para abrir a lojinha
def abrir_lojinha():
    global loja  # Adiciona uma variável global para a loja
    loja = tk.Toplevel(root)
    loja.title("Lojinha de Bananas")
    atualizar_loja()

# Função para atualizar os preços na loja
def atualizar_loja():
    for widget in loja.winfo_children():
        widget.destroy()
    
    # Botão para comprar auto-clique
    btn_auto_click = tk.Button(loja, text=f"Comprar Auto-Clique ({auto_click_custo} Bananas Amarelas)", command=comprar_auto_click)
    btn_auto_click.pack(pady=10)
    
    # Botão para comprar maior chance de banana rara
    btn_banana_rara = tk.Button(loja, text="Comprar Maior Chance de Banana Rara (30 Bananas Verdes)", command=comprar_banana_rara)
    btn_banana_rara.pack(pady=10)

    # Botão para comprar duplicador de bananas
    btn_duplicador = tk.Button(loja, text="Comprar Duplicador de Bananas (20 Bananas Azuis)", command=comprar_duplicador)
    btn_duplicador.pack(pady=10)

    # Botão para comprar triplificador de bananas
    btn_triplificador = tk.Button(loja, text="Comprar Triplificador de Bananas (15 Bananas Vermelhas)", command=comprar_triplificador)
    btn_triplificador.pack(pady=10)
    
    # Botão para ativar/desativar auto-clique
    btn_toggle_auto_click = tk.Button(loja, text="Ativar/Desativar Auto-Clique", command=toggle_auto_click)
    btn_toggle_auto_click.pack(pady=10)

# Função para comprar auto-clique
def comprar_auto_click():
    global auto_click_speed, auto_click_custo
    if banana_contagem["amarela"] >= auto_click_custo:
        banana_contagem["amarela"] -= auto_click_custo
        upgrades["auto_click"] = True
        auto_click_speed = max(100, auto_click_speed // 2)  # Reduz a velocidade pela metade, mínimo de 100 ms
        auto_click_custo *= 2  # Dobra o custo a cada compra
        atualizar_placar()
        resultado['text'] = "Auto-Clique comprado!"
        atualizar_loja()

# Função para comprar maior chance de banana rara
def comprar_banana_rara():
    if banana_contagem["verde"] >= 30:
        banana_contagem["verde"] -= 30
        upgrades["banana_rara"] = True
        atualizar_placar()
        resultado['text'] = "Maior chance de banana rara comprada!"
        atualizar_loja()

# Função para comprar duplicador de bananas
def comprar_duplicador():
    if banana_contagem["azul"] >= 20:
        banana_contagem["azul"] -= 20
        upgrades["duplicador"] += 1
        atualizar_placar()
        resultado['text'] = "Duplicador de Bananas comprado!"
        atualizar_loja()

# Função para comprar triplificador de bananas
def comprar_triplificador():
    if banana_contagem["vermelha"] >= 15:
        banana_contagem["vermelha"] -= 15
        upgrades["triplificador"] += 1
        atualizar_placar()
        resultado['text'] = "Triplificador de Bananas comprado!"
        atualizar_loja()

# Função para ativar/desativar auto-clique
def toggle_auto_click():
    upgrades["auto_click"] = not upgrades["auto_click"]
    estado = "ativado" if upgrades["auto_click"] else "desativado"
    resultado['text'] = f"Auto-Clique {estado}!"

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Bananas Aleatórias")

# Botão
btn = tk.Button(root, text="Clique para ganhar uma banana", command=gerar_banana)
btn.pack(pady=20)

# Label para mostrar o resultado
resultado = tk.Label(root, text="")
resultado.pack(pady=20)

# Botão para abrir a lojinha
btn_loja = tk.Button(root, text="Abrir Lojinha", command=abrir_lojinha)
btn_loja.pack(pady=20)

# Placar
placar_amarelo = tk.Label(root, text=f"Bananas Amarelas: {banana_contagem['amarela']}")
placar_amarelo.pack(pady=5)

placar_verde = tk.Label(root, text=f"Bananas Verdes: {banana_contagem['verde']}")
placar_verde.pack(pady=5)

placar_azul = tk.Label(root, text=f"Bananas Azuis: {banana_contagem['azul']}")
placar_azul.pack(pady=5)

placar_vermelho = tk.Label(root, text=f"Bananas Vermelhas: {banana_contagem['vermelha']}")
placar_vermelho.pack(pady=5)

# Execução da interface gráfica
root.mainloop()
