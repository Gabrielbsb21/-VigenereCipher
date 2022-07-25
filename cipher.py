from key_generator import key_generator

def cipher (password, message):

    message = message.replace(',', "").replace(
        '.', "").replace(" ", "").lower()
    size = len(message)
    key = key_generator(password, size)
    message_number = [ord(letra) - 97 for letra in message]
    key_number = [ord(letra) - 97 for letra in key]

    cipher_message = []
    j = 0

    for i in range(size):
        if message_number[i] == (-65):

            cipher_message.append(32)

        else:

            cipher_message.append(
                ((message_number[i] + key_number[j]) % 26)+97)
            j = j+1

    fim = "".join([chr(c) for c in cipher_message])

    return fim
