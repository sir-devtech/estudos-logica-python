# Expressões aritméticas
# Cálculo de dano simples.

ataque = float(input("Ataque base: "))
bonus = float(input("Bônus de arma: "))
inimigos = int(input("Quantidade de inimigos: "))

dano_total = (ataque + bonus) * inimigos
media = dano_total / inimigos if inimigos else 0

print(f"Dano total: {dano_total}")
print(f"Dano médio por inimigo: {media}")
