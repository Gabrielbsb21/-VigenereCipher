from decipher import decipher
from key_generator import key_generator 
from freq import pega_frequencia_ing
from freq import pega_frequencia_ptbr
# ------------------------------------------------

def ataque(cifra):
    
    # seleciona lingua
    op = int(input("Deseja usar frequências das letras em Inglês(1) ou Português(2)?\n"))
    
    # pegar frequências de grupos de 3 letras
    # ------------------------------------------------

    itens = []
    # itens = [letras analizadas1, vezes que repetiu1, distancia1, letras analizadas2, vezes que repetiu2, distancia2...]
    
    tamanho = len(cifra)
    letras = "" # grupo de letras inicia vazio
    j = 0   # contador de grupos de 3 letras inicia em zero
    repeticao = 0   # variavel que guarda repeticao inicia em zero
    dist = 0 # distancia entre repetições
    
    for i in range(tamanho):
        
        # se estamos dentro do grupo de 3 letras, e a cifra não é espaço vazio, atualiza as letras de analise
        if cifra[i] != " " and j < 3:
            letras = letras + cifra[i]
            j = j + 1
        
        dist_sem_espaco = 0
            
        # caso já seja conhecido o grupo de 3 letras a ser analizado
        if j == 3:
            # varre a string da cifra inteira vendo quantas vezes o grupo de letras se repetiu
            for a in range(tamanho):
                
                if cifra[a] != " ":
                    dist_sem_espaco = dist_sem_espaco + 1 
                
                if a < (tamanho - 3):
                    
                    # salvamos a quantidade de vezes que repetiu
                    if cifra[a] == letras[0]:
                        if((cifra[a+1] == " ")):
                            
                            # achamos uma repetição e ignoramos o espaço no meio: "a bc"
                            if((cifra[a+2] == letras[1]) and (cifra[a+3] == letras[2])):
                                
                                # queremos salvar a distância entre repetições!
                                # se é a primeira repetição, guarda onde ela ocorreu
                                # se é a segunda, pega a diferença de posição atual e primeira ocorrência
                                if(repeticao == 0):
                                    primeira_ocorrencia = dist_sem_espaco
                                if(repeticao > 0):
                                    dist = dist_sem_espaco - primeira_ocorrencia    
                                repeticao = repeticao + 1
                                
                        else:
                            
                            # achamos uma repeticao das 3 letras sem o espaço "abc"
                            if((cifra[a+1] == letras[1]) and (cifra[a+2] == letras[2])):
                                
                                # guardamos resultado de distância
                                if(repeticao == 0):
                                    primeira_ocorrencia = dist_sem_espaco
                                if(repeticao > 0):
                                    dist = dist_sem_espaco - primeira_ocorrencia     
                                repeticao = repeticao + 1
                                
                            if((cifra[a+2] == " ")):  
                                # achamos a repetição das 3 letras, com um espaço no final: "ab c"
                                if((cifra[a+1] == letras[1]) and (cifra[a+3] == letras[2])):
                                    
                                    # guardamos resultado de distância
                                    if(repeticao == 0):
                                        primeira_ocorrencia = dist_sem_espaco
                                    if(repeticao > 0):
                                        dist = dist_sem_espaco - primeira_ocorrencia     
                                    repeticao = repeticao + 1  

            # se o grupo de letras repetiu em algum ponto, salvamos
            if repeticao != 0:
                itens.append(letras)
                itens.append(repeticao)
                itens.append(dist)
                    
            j = 0 # zera contador
            letras = "" # esvazia string
            repeticao = 0 # zera repeticao
            dist = 0 # zera distancia
    
    # mostramos o resultado da análise de letras em grupos
    # ------------------------------------------------
    
    tamanho_rep = len(itens)
    quantidade_reps = int(tamanho_rep/3)
        
    print("Analizou-se " + str(quantidade_reps) + "grupos de letras!\n")
    
    j = 0
    for i in range(quantidade_reps):
        print("Grupo de letras: " + str(itens[j]))   
        j = j + 1
        print("Vezes que repetiu: " + str(itens[j]))
        j = j + 1 
        print("Distância entre repetição: " + str(itens[j]) + "\n")
        
        mod = 1
        if itens[j] != 0:
            for k in range(10):
                if k != 0:
                    mod = (itens[j] % k)
                if mod == 0: 
                    print("Distância diviśivel por " + str(k))
        j = j + 1

    tamanho_key_chute = int(input("\n\nSugestão para o tamanho da key diante desta análise?\nInforme um número inteiro por favor.\nTenha como base os números dados préviamente, vendo qual número geralmente um conjunto de letras é divisível com maior frequência.\n\n"))

    # analizar frequencia de letras da lingua
    # ------------------------------------------------


    # digamos, a key tem tamanho 6
    # se analisa a posição x dentro desse tamanho 6, pois a posição x a cada 6 letras sofreu o mesmo deslocamento
    # mesmo deslocamento, mesma frequencia da língua escolhida, possibilitando um bom chute

    # Inglês
    if op == 1:
        
        print("Iniciando análise para texto em Inglês!")
        
        # faz isso para cada letra "y" dentro do tamanho da sugestão de chave, pega um input com sugestão do deslocamento 
        for j in range(tamanho_key_chute):
            print("\n\nANÁLISE PARA POSIÇÃO " + str(j) + " NA CIFRA DE TAMANHO SUGERIDO " + str(tamanho_key_chute))
            frequencia = pega_frequencia_ing(cifra, tamanho_key_chute, j)
        
    # Português    
    if op == 2:
        
        print("Iniciando análise para texto em Português!")
        # faz isso para cada letra "y" dentro do tamanho da sugestão de chave, pega um input com sugestão do deslocamento 
        for j in range(tamanho_key_chute):
            print("\n\nANÁLISE PARA POSIÇÃO " + str(j) + " NA CIFRA DE TAMANHO SUGERIDO " + str(tamanho_key_chute))
            frequencia = pega_frequencia_ptbr(cifra, tamanho_key_chute, j)
        
    
    # Idioma inválido    
    if((op != 1) and (op != 2)):
        print("Selecione uma opção válida, encerrando programa")

    return 0
