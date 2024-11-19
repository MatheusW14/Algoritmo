def area_terangulo(base, altura):
    return (base * altura)/ 2

print(f"Digite os valores da base e altura de um retângulo, para descobrirmos sua área:")

base = float(input("Digite a área: "))
altura = float(input("Digite a altura: "))

area = area_terangulo(base, altura)
print(f"A área do retângulo é {area}")
    