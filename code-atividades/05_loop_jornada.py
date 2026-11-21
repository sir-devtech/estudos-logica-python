# Loops (for / while)
# Conta os dias da jornada.

dias = int(input("Quantos dias de marcha? "))

print("--- for ---")
for dia in range(1, dias + 1):
    print(f"Dia {dia}: um passo a mais.")

print("--- while ---")
restantes = dias
while restantes > 0:
    print(f"Faltam {restantes} dia(s).")
    restantes -= 1

print("Acampamento.")
