import tkinter as tk

#funcao que calcula o custo
def calcular_custo():
    valorPorPalavra=float(valorPorPalavra_entry.get())
    totalPalavras=int(totalPalavras_entry.get())
    custoTotal=(valorPorPalavra*totalPalavras)/100
    custo_label.config(text=f"Custo Total: R$ {custoTotal:.2f}")
    
#criando a GUI
root = tk.Tk()
root.geometry("300x100")
root.title("Calc Custo por Palavra")

#criando os widgets
tk.Label(root,text="Valor por palavra (centavos):").pack()
valorPorPalavra_entry = tk.Entry(root)
valorPorPalavra_entry.pack()

tk.Label(root, text="Total de Palavra:").pack()
totalPalavras_entry =tk.Entry(root)
totalPalavras_entry.pack()

tk.Button(root, text="Calcular", command=calcular_custo).pack()

#exibindo o resultado
custo_label=tk.Label(root, text="Custo Total: R$ 0.00")
custo_label.pack()

#iniciando o loop
root.mainloop()