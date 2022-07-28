def pega_frequencia_ing(cifra, tamanho_chave, intervalo):

    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    freq_cifra = []

    freq_alfabeto = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025,
                     2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

    for i in range(26):
        freq_cifra.append(0)

    # print(freq_cifra)

    # posição [0] é a quantidade de vezes que o "a" repetiu
    # posição [1] é a quantidade de vezes que o "b" repetiu
    # ...
    # posição [25] é a quantidade de vezes que o "z" repetiu

    j = 0
    quantidade_de_resets = 0

    for i in range(len(cifra)):

        if(cifra[i] != " "):

            if(j == tamanho_chave):
                # reset
                j = 0
                quantidade_de_resets = quantidade_de_resets + 1

            if(j == intervalo):
                # salva a ocorrencia da letra
                letra = (ord(cifra[i]) - 97)
                # print("letra!")
                # print(letra)
                freq_cifra[letra] = freq_cifra[letra] + 1
                letra = 0

            j = j + 1

    print("Frequência encontrada: ")
    for i in range(26):
        porcentagem = round((freq_cifra[i]/quantidade_de_resets)*100, 2)
        print("Frequencia da Letra '" + alfabeto[i] + "' na cifra: " + str(
            porcentagem) + "%, Frequência original: " + str(freq_alfabeto[i]) + "%")

    maior_freq = 0.0
    letra_mais_repetida = 0

    for i in range(26):

        porcentagem = round((freq_cifra[i]/quantidade_de_resets)*100, 2)

        if(porcentagem > maior_freq):

            segunda_maior_freq = maior_freq
            segunda_letra_mais_repetida = letra_mais_repetida

            maior_freq = porcentagem
            letra_mais_repetida = i

    print("Letra com mais repetição na cifra é: " +
          alfabeto[letra_mais_repetida])
    print("Segunda Letra com mais repetição na cifra é: " +
          alfabeto[segunda_letra_mais_repetida])

    print("Originalmente, letras mais repetidas são 'a',  'e' e por fim 't'")
    print("---------------------------------------")
    print("\nLista de sugestões (em ordem) para a letra nessa posição da cifra, batendo o deslocamento entre letra com maior frequência!\n")

    # calculando deslocamento de "e"

    dif = 4 - letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    dif = 4 - segunda_letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    # calculando deslocamento de "t"

    dif = 19 - letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    dif = 19 - segunda_letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    # deslocamento de é "a" diferença de zero, logo é a própria frequência
    print("Sugestão de letra para cifra: " + alfabeto[letra_mais_repetida])
    print("Sugestão de letra para cifra: " +
          alfabeto[segunda_letra_mais_repetida])
    print("---------------------------------------")

    return 0

# PORTUGUÊS
# ------------------------------------------------


def pega_frequencia_ptbr(cifra, tamanho_chave, intervalo):

    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    freq_cifra = []

    freq_alfabeto = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78,
                     4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]

    for i in range(26):
        freq_cifra.append(0)

    # print(freq_cifra)

    # posição [0] é a quantidade de vezes que o "a" repetiu
    # posição [1] é a quantidade de vezes que o "b" repetiu
    # ...
    # posição [25] é a quantidade de vezes que o "z" repetiu

    j = 0
    quantidade_de_resets = 0

    for i in range(len(cifra)):

        if cifra[i] != " ":

            if j == tamanho_chave:
                # reset
                j = 0
                quantidade_de_resets = quantidade_de_resets + 1

            if j == intervalo:
                # salva a ocorrencia da letra
                letra = (ord(cifra[i]) - 97)
                # print("letra!")
                # print(letra)
                freq_cifra[letra] = freq_cifra[letra] + 1
                letra = 0

            j = j + 1

    print("Frequência encontrada: ")
    for i in range(26):
        porcentagem = round((freq_cifra[i]/quantidade_de_resets)*100, 2)
        print("Frequencia da Letra '" + alfabeto[i] + "' na cifra: " + str(
            porcentagem) + "%, Frequência original: " + str(freq_alfabeto[i]) + "%")

    maior_freq = 0.0
    letra_mais_repetida = 0

    for i in range(26):

        porcentagem = round((freq_cifra[i]/quantidade_de_resets)*100, 2)

        if(porcentagem > maior_freq):

            segunda_maior_freq = maior_freq
            segunda_letra_mais_repetida = letra_mais_repetida

            maior_freq = porcentagem
            letra_mais_repetida = i

    print("Letra com mais repetição na cifra é: " +
          alfabeto[letra_mais_repetida])
    print("Segunda Letra com mais repetição na cifra é: " +
          alfabeto[segunda_letra_mais_repetida])

    print("Originalmente, letras mais repetidas são 'a',  'e' e por fim 'o'")
    print("---------------------------------------")
    print("\nLista de sugestões (em ordem) para a letra nessa posição da cifra, batendo o deslocamento entre letra com maior frequência!\n")

    # calculando deslocamento de "a"
    print("Sugestão de letra para cifra: " + alfabeto[letra_mais_repetida])
    print("Sugestão de letra para cifra: " +
          alfabeto[segunda_letra_mais_repetida])

    # calculando deslocamento de "e"
    dif = 4 - letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    dif = 4 - segunda_letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    # deslocamento de é "o" diferença de zero, logo é a própria frequência

    dif = 14 - letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])

    dif = 14 - segunda_letra_mais_repetida

    if (dif < 0):
        dif = dif * (-1)

    print("Sugestão de letra para cifra: " + alfabeto[dif])
    print("---------------------------------------")

    return 0
