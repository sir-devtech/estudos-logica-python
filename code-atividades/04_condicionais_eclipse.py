# Condicionais (if / elif / else)
# Decide o rumo conforme o nível de ameaça.

ameaca = int(input("Nível de ameaça (0-100): "))

if ameaca >= 80:
    print("Eclipse iminente. Fuja ou lute com tudo.")
elif ameaca >= 40:
    print("Perigo médio. Mantenha a espada pronta.")
else:
    print("Trilha calma. Ainda dá pra respirar.")
