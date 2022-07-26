import time 

def save (msg):

    print("Deseja salvar o resultado em um arquivo de texto?[Y/N]?")
    salvar = input()

    if salvar == 'y' or salvar == 'Y':

        nome_arquivo = "resultado_cifrado" + str(time.time())
    
        arquivo = open(nome_arquivo, 'w+')

        arquivo.writelines("Resultado cifrado: " + msg)

        arquivo.close()

        print("Arquivo salvo!")

    return 0