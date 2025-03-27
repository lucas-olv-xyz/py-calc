# Calculadora de Palavras e Custos

Esta aplicação desktop, desenvolvida com Tkinter e ttk, permite o cálculo do total de palavras adicionadas e o valor total com base em um custo por palavra informado (em centavos). A interface gráfica possibilita o registro incremental de palavras, o cálculo do valor final e a reinicialização dos valores.

---

## Funcionalidades

- **Adicionar Palavras:** Insira a quantidade de palavras e adicione ao total.
- **Calcular Valor Total:** Informe o custo por palavra (em centavos) e calcule o valor total.
- **Reset:** Reinicia o total de palavras e o valor total.

---

## Tecnologias e Bibliotecas Utilizadas

- **tkinter:** Biblioteca padrão do Python para criação de interfaces gráficas.
- **ttk:** Módulo do tkinter que oferece widgets com temas mais modernos e configuráveis.

---

## Como Executar

1. **Pré-requisitos:**

   - Python 3.x instalado.
   - Tkinter (geralmente incluído na instalação padrão do Python).

2. **Salve o script** em um arquivo, por exemplo, `calculadora.py`.

3. **Execute o script**:

   ```bash
   python calculadora.py
   ```

4. A janela da aplicação será aberta, permitindo a interação com os campos e botões.

---

## Estrutura do Código

- **Interface Gráfica:** Configuração da janela, layout com grid e estilização dos widgets (Labels, Buttons e Entries).
- **Funções:**
  - `adicionar_ao_total`: Adiciona a quantidade informada ao total de palavras.
  - `calcular_valor_total`: Converte o valor por palavra de centavos para reais e calcula o total.
  - `reset`: Reinicia os campos e os valores exibidos.

---

## Exemplo de Uso

1. Informe a quantidade de palavras no campo "Quantidade de palavras:" e clique em "Adicionar ao Total".
2. Visualize a atualização do total de palavras.
3. Insira o valor por palavra (em centavos) e clique em "Calcular Valor Total" para ver o valor final em reais.
4. Clique em "Reset" para limpar os campos e reiniciar o total.

---
