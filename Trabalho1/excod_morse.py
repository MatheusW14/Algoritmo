morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.','G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  
}

def frase_para_morse(frase):
    frase = frase.upper() 
    morse_frase = ''
    
    for letra in frase:
        if letra in morse_code:
            morse_frase += morse_code[letra] + ' ' # o (+ ' ') coloca um espaço após cada Morse para separar as letras.
        else:
            morse_frase += '?'  # coloca interrogação se o caractere não estiver no dicionário.
    return morse_frase.strip() # .strip() remove o espaço final.


frase = input("Digite uma frase para converter em código Morse: ")
resultado = frase_para_morse(frase)
print(f"Código Morse:{resultado}")
