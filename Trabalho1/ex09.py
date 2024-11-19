def verificador_maior_idade(idade):
    if idade >= 18:
        return True
    else: 
        return False
    
idade = int(input(f'Digite sua idade para verificação:'))
            
if verificador_maior_idade(idade) == True:
    print(f"Você é maior de idade!")
else: 
    print(f"Você não é maior de idade")


