import tkinter as tk
from tkinter import ttk
import threading
import random
import time

# Variáveis globais dos sensores
sensor_data = {
    "temperatura": 25,
    "luminosidade": 300,
    "presenca": False
}

# Estado dos atuadores
atuadores = {
    "ar_condicionado": False,
    "lampada": False,
    "fechadura": True  # True = Fechada
}

# Funções de controle dos atuadores
def controlar_ar_condicionado():
    if sensor_data["temperatura"] > 28:
        atuadores["ar_condicionado"] = True
    else:
        atuadores["ar_condicionado"] = False

def controlar_lampada():
    if sensor_data["luminosidade"] < 200 or sensor_data["presenca"]:
        atuadores["lampada"] = True
    else:
        atuadores["lampada"] = False

def atualizar_atuadores_auto():
    controlar_ar_condicionado()
    controlar_lampada()

# Simulador de sensores
def atualizar_sensores():
    while True:
        sensor_data["temperatura"] = random.randint(20, 35)
        sensor_data["luminosidade"] = random.randint(100, 500)
        sensor_data["presenca"] = random.choice([True, False])
        atualizar_atuadores_auto()
        time.sleep(2)

# Atualizar GUI com dados
def atualizar_gui():
    lbl_temp_val.config(text=f'{sensor_data["temperatura"]} °C')
    lbl_luz_val.config(text=f'{sensor_data["luminosidade"]} lux')
    lbl_pres_val.config(text="Sim" if sensor_data["presenca"] else "Não")

    lbl_ar_val.config(text="Ligado" if atuadores["ar_condicionado"] else "Desligado")
    lbl_lampada_val.config(text="Ligada" if atuadores["lampada"] else "Desligada")
    lbl_fechadura_val.config(text="Fechada" if atuadores["fechadura"] else "Aberta")

    root.after(1000, atualizar_gui)

# Controles manuais
def alternar_fechadura():
    atuadores["fechadura"] = not atuadores["fechadura"]

# GUI com tkinter
root = tk.Tk()
root.title("Simulador de Casa Inteligente")
root.geometry("400x300")

# Sensores
ttk.Label(root, text="Sensores", font=("Helvetica", 14)).pack()
lbl_temp_val = ttk.Label(root, text="-- °C")
lbl_luz_val = ttk.Label(root, text="-- lux")
lbl_pres_val = ttk.Label(root, text="--")

ttk.Label(root, text="Temperatura:").pack()
lbl_temp_val.pack()
ttk.Label(root, text="Luminosidade:").pack()
lbl_luz_val.pack()
ttk.Label(root, text="Presença:").pack()
lbl_pres_val.pack()

# Atuadores
ttk.Label(root, text="Atuadores", font=("Helvetica", 14)).pack(pady=(10, 0))
lbl_ar_val = ttk.Label(root, text="--")
lbl_lampada_val = ttk.Label(root, text="--")
lbl_fechadura_val = ttk.Label(root, text="--")

ttk.Label(root, text="Ar-condicionado:").pack()
lbl_ar_val.pack()
ttk.Label(root, text="Lâmpada:").pack()
lbl_lampada_val.pack()
ttk.Label(root, text="Fechadura:").pack()
lbl_fechadura_val.pack()

ttk.Button(root, text="Alternar Fechadura", command=alternar_fechadura).pack(pady=5)

# Inicia thread dos sensores
thread_sensor = threading.Thread(target=atualizar_sensores, daemon=True)
thread_sensor.start()

# Inicia loop da GUI
root.after(1000, atualizar_gui)
root.mainloop()