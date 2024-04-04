import tkinter as tk

def calcular_custo():
    valor_por_palavra = float(valor_por_palavra_entry.get())
    total_palavras = int(total_palavras_entry.get())
    custo_total = (valor_por_palavra * total_palavras) / 100  # Convertendo para reais
    custo_label.config(text=f"Custo Total: R$ {custo_total:.2f}")

# Configuração da janela
root = tk.Tk()
root.title("Calculadora de Custo por Palavra")

# Layout
tk.Label(root, text="Valor por palavra (centavos):").pack()
valor_por_palavra_entry = tk.Entry(root)
valor_por_palavra_entry.pack()

tk.Label(root, text="Total de palavras:").pack()
total_palavras_entry = tk.Entry(root)
total_palavras_entry.pack()

tk.Button(root, text="Calcular", command=calcular_custo).pack()

custo_label = tk.Label(root, text="Custo Total: R$ 0.00")
custo_label.pack()

# Iniciando a aplicação
root.mainloop()
