# Funções
# Contribuição: encapsula o cálculo da "marca" (score simples).


def calcular_marca(forca, vontade):
    return forca * 2 + vontade


forca = int(input("Força: "))
vontade = int(input("Vontade: "))
print(f"Marca calculada: {calcular_marca(forca, vontade)}")
