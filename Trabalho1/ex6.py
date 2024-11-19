def media_final(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

print(f'Digite suas 3 notas:')

nota1 = (float(input()))
nota2 = (float(input()))
nota3 = (float(input()))

media = media_final(nota1, nota2, nota3)
print(f'Sua média final é: {media:.2f}')