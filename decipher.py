from key_generator import key_generator


def decipher(cipher, key):

    size = len(cipher)
    key = key_generator(key, size)

    cifra_num = [ord(letra) - 97 for letra in cipher]

    key_num = [ord(letra) - 97 for letra in key]

    msg_decifrada_num = []

    j = 0

    for i in range(size):

        if(cifra_num[i] == (-65)):

            msg_decifrada_num.append(32)

        else:

            msg_decifrada_num.append(((cifra_num[i] - key_num[j]) % 26)+97)
            j = j+1
    fim = "".join([chr(c) for c in msg_decifrada_num])

    return fim
