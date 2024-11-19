def media_final(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def notas_maiores_que_media(nota1, nota2, nota3):
    media = media_final(nota1, nota2, nota3)
    notas = [nota1, nota2, nota3]
    return [nota for nota in notas if nota > media]  

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = media_final(nota1, nota2, nota3)
maiores_que_media = notas_maiores_que_media(nota1, nota2, nota3)

print(f"A média das notas é: {media:.2f}")
print(f"As notas maiores que a média são: {maiores_que_media}")