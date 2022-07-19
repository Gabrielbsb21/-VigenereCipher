def key_generator(key, size):

    # divide o tamanho que queremos com o tamanho atual, arredonda pra +1
    repetitions = size // len(key) + 1

    # repete a chave "x" vezes
    repeated_key = key * repetitions

    # corta no tamanho desejado
    correct_key = repeated_key[:size]

    # retorna o que sobrou
    return correct_key