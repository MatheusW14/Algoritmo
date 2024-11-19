def gerar_fibonacci(n):
    fibonacci = [0, 1]  
    for i in range(2, n):  
        fibonacci.append(fibonacci[-1] + fibonacci[-2])  # soma dos dois últimos numeros.
    return fibonacci[:n]  # o [:n] é um slicing(fatiamento), pra garantir que sempre retorne o numero(n) solicitado.


n = int(input("Digite o valor de n para gerar a sequência de Fibonacci: "))


sequencia_fibonacci = gerar_fibonacci(n)


print(f"A sequência de Fibonacci com {n} números é: {sequencia_fibonacci}")
