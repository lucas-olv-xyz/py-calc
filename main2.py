import tkinter as tk
from tkinter import ttk  # Importando ttk para usar os widgets com temas.

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Palavras e Custos")
        self.root.geometry("500x350")  # Aumentando um pouco o tamanho da janela
        
        # Configurações de estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TEntry', font=('Arial', 12), padding=5)
        
        # Variáveis
        self.total_palavras = 0
        
        # Layout usando grid
        ttk.Label(self.root, text="Quantidade de palavras:").grid(column=0, row=0, padx=10, pady=5, sticky="w")
        self.quantidade_palavras_entry = ttk.Entry(self.root)
        self.quantidade_palavras_entry.grid(column=1, row=0, padx=10, pady=5, sticky="ew")
        
        ttk.Button(self.root, text="Adicionar ao Total", command=self.adicionar_ao_total).grid(column=0, row=1, columnspan=2, padx=10, pady=5, sticky="ew")
        
        self.total_palavras_label = ttk.Label(self.root, text="Total de Palavras: 0")
        self.total_palavras_label.grid(column=0, row=2, columnspan=2, padx=10, pady=5, sticky="w")
        
        ttk.Label(self.root, text="Valor por palavra (centavos):").grid(column=0, row=3, padx=10, pady=5, sticky="w")
        self.valor_por_palavra_entry = ttk.Entry(self.root)
        self.valor_por_palavra_entry.grid(column=1, row=3, padx=10, pady=5, sticky="ew")
        
        ttk.Button(self.root, text="Calcular Valor Total", command=self.calcular_valor_total).grid(column=0, row=4, columnspan=2, padx=10, pady=5, sticky="ew")
        
        self.valor_total_label = ttk.Label(self.root, text="Valor Total: R$ 0.00")
        self.valor_total_label.grid(column=0, row=5, columnspan=2, padx=10, pady=5, sticky="w")

        ttk.Button(self.root, text="Reset", command=self.reset).grid(column=0, row=6, columnspan=2, padx=10, pady=5, sticky="ew")

        # Fazendo com que a coluna 1 expanda para preencher o espaço extra
        self.root.grid_columnconfigure(1, weight=1)

    def adicionar_ao_total(self):
        quantidade = int(self.quantidade_palavras_entry.get())
        self.total_palavras += quantidade
        self.total_palavras_label.config(text=f"Total de Palavras: {self.total_palavras}")
        self.quantidade_palavras_entry.delete(0, tk.END)  # Limpa o campo de entrada

    def calcular_valor_total(self):
        valor_por_palavra = float(self.valor_por_palavra_entry.get()) / 100  # Convertendo para reais
        valor_total = self.total_palavras * valor_por_palavra
        self.valor_total_label.config(text=f"Valor Total: R$ {valor_total:.2f}")

    def reset(self):
        self.total_palavras = 0
        self.quantidade_palavras_entry.delete(0, tk.END)
        self.valor_por_palavra_entry.delete(0, tk.END)
        self.total_palavras_label.config(text="Total de Palavras: 0")
        self.valor_total_label.config(text="Valor Total: R$ 0.00")

root = tk.Tk()
app = App(root)
root.mainloop()
