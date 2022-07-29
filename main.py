from cipher import cipher
from decipher import decipher
from save import save
from attack import attack

print("Operações disponíveis: \n1- Cifrar\n2- Decifrar\n3- Atacar\n ")
print("Que operação deseja realizar?")
chosen_option = int(input())

if chosen_option == 1:
    print("Digite sua senha")
    password = input()
    print("Digite sua mensagem")
    message = input()
    cifrada = cipher(password, message)
    save(cifrada)
    print(cifrada)
elif chosen_option == 2:
    print("Digite sua cifra")
    cifra = input()
    print("Digite sua senha")
    password = input()
    decifrado = decipher(cifra, password)
    save(decifrado)
    print (decifrado)
elif chosen_option == 3:
    print("Digite sua cifra")
    cifra = input()
    cifra = cifra.lower()   # trabalhando com letras minusculas, sem caracteres especiais
    cifra = cifra.replace(',', "").replace('.', "").replace('-', "").replace('"', "").replace(':', "").replace(';', "").replace("'", "")

    resultado = attack(cifra)
else:
    print("Operação Inválida")