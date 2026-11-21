# Listas
# Inventário do guerreiro.

equipamento = []
qtd = int(input("Quantos itens vai carregar? "))

for i in range(qtd):
    item = input(f"Item {i + 1}: ")
    equipamento.append(item)

print("Inventário:", equipamento)
print("Primeiro item:", equipamento[0] if equipamento else "(vazio)")
print("Total de itens:", len(equipamento))
