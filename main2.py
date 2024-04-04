import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Palavras e Custos")
        self.root.geometry("500x300")
        
        # Variáveis
        self.total_palavras = 0
        
        # Layout
        tk.Label(self.root, text="Quantidade de palavras:").pack()
        self.quantidade_palavras_entry = tk.Entry(self.root)
        self.quantidade_palavras_entry.pack()
        
        tk.Button(self.root, text="Adicionar ao Total", command=self.adicionar_ao_total).pack()
        
        self.total_palavras_label = tk.Label(self.root, text="Total de Palavras: 0")
        self.total_palavras_label.pack()
        
        tk.Label(self.root, text="Valor por palavra (centavos):").pack()
        self.valor_por_palavra_entry = tk.Entry(self.root)
        self.valor_por_palavra_entry.pack()
        
        tk.Button(self.root, text="Calcular Valor Total", command=self.calcular_valor_total).pack()
        
        self.valor_total_label = tk.Label(self.root, text="Valor Total: R$ 0.00")
        self.valor_total_label.pack()

    def adicionar_ao_total(self):
        quantidade = int(self.quantidade_palavras_entry.get())
        self.total_palavras += quantidade
        self.total_palavras_label.config(text=f"Total de Palavras: {self.total_palavras}")
        self.quantidade_palavras_entry.delete(0, tk.END)  # Limpa o campo de entrada

    def calcular_valor_total(self):
        valor_por_palavra = float(self.valor_por_palavra_entry.get()) / 100  # Convertendo para reais
        valor_total = self.total_palavras * valor_por_palavra
        self.valor_total_label.config(text=f"Valor Total: R$ {valor_total:.2f}")

root = tk.Tk()
app = App(root)
root.mainloop()
