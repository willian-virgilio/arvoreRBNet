
from ArvRB import ArvRB
from collections import Counter
import datetime

versao = []

sucessor = []

vetor = []

nova = ArvRB()


class Arquivo:



    def __init__(self,nomeArqv):
        self.nomeArqv = nomeArqv
        self.smsErro = False




    def lerArquivo(self):
        abrir_arquivo = open('entrada.txt', 'r')
        for comando in abrir_arquivo:
            comando = comando.rstrip()
            print("Valores de comando:",comando)
            vetor.append(comando)
        abrir_arquivo.close()

    def loopDeGravacao(self,x):

        arqv_saida = open('saida.txt', 'w')
        for i in range(len(x)):
            a = x[i]
            arqv_saida.write(a + ' ')
        arqv_saida.write('\n')

    def smsdeErro(self,sms):

        self.smsErro = 'V'



    def gravarCorrigido(self,corrigido,index,elemento):
        arqv_saida = open('saida.txt', 'a')
        if (int(corrigido) < int(index)):
            arqv_saida.write(index + ' ')
            arqv_saida.write(str(corrigido) + ' ')
            arqv_saida.write('\n')
        else:
            arqv_saida.write(index + ' ')
            arqv_saida.write(elemento + ' ')
            arqv_saida.write('\n')


    def testeEscrita(self):
       # print(self.controle_versao)
        msg_erro_index = "Erro : Valor a ser inserido ou removido é inexistente, \n" \
                         "ou a operação  contem algum caracter invalido" \
                        "O arquivo entrada.txt contem uma instrução invalida, \n " \
                        "Verifique as seguntes possibilidades:\n" \
                        " 1 - Se alguma instrução esta faltando numero posterior a ela. \n" \
                        "Exemplo: INC  <-----está sem o numero da versão!!\n" \
                        "    2 - Se contem caracter invalido, não numerico.: Exemplo REM x \n"

        print("Tamanho do vetor1: ",len(vetor))
        arqv_saida = open('saida.txt', 'a')
        arqv_saida.truncate(0)



        for i in range(0,len(vetor),1):

            # O primeiro elemento da lista separador é o comando, o segundo é o valor lista_comandos_e_valores = [0]
            lista_comandos_e_valores = vetor[i].split()
            print("toda a lista :",lista_comandos_e_valores)
           # print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))

            # primeiro if, caso o vetor1addr tenha indices maior que 2, então ele é o comando SUC de sucessor
            if( len(lista_comandos_e_valores) > 2):
              #  print("O sucessor de: "+ lista_comandos_e_valores[1]+ " é: ")
              #  print("A versão da estrutura é :", lista_comandos_e_valores[2])
                #print(lista_comandos_e_valores)
                nversao = (int(lista_comandos_e_valores[2]))
                print("A versão de busca do sucessor é:", nversao)
                elemento = int(lista_comandos_e_valores[1])

                a = nova.retornar_versao(nversao,True,'')
               # if (c >= lista_comandos_e_valores[2] ):
                #    arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                 #   arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                  #  arqv_saida.write(lista_comandos_e_valores[c] + ' ')

               # print("Elementos salvos desta  versão: ",a)
                print("O valor de pesquisa de sucessor: ",elemento)

                corrigido = nova.retornar_valor_corrigido()
                print("Tipo corrigido: ",type(corrigido))
                print("Valor corrigido: ", corrigido)
                print("Valor da versão solicitada ", lista_comandos_e_valores[2])
                arqv_saida.write('SUC ')

                if (int(corrigido) < int(lista_comandos_e_valores[2])):
                    arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                    arqv_saida.write(str(corrigido) + ' ')
                    arqv_saida.write('\n')
                else:
                    arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                    arqv_saida.write(lista_comandos_e_valores[2] + ' ')
                    arqv_saida.write('\n')
               # nova.buscar_sucessor(int(lista_comandos_e_valores[1]),int(lista_comandos_e_valores[2]))

                sucessor.clear()

                # if(len(a) == 0)
                print('Vetor A:',a)
                for i in range(0,len(a),4):

                    if(int(lista_comandos_e_valores[1]) < int(a[i]) ):


                        sucessor.append(int(a[i]))
#

                    print("lista de valores de sucessores:", sucessor)
                    print("tamanho", len(sucessor))

                    x = 0
                    for i in range(len(sucessor)):
                        x = min(sucessor)

                    if(x == 0 ):
                        x = 'INF'
                    print("este é o sucessor", x)


                arqv_saida.write(str(x))

                arqv_saida.write('\n')
            # verificar erro AttributeError: 'str' object has no attribute 'loopDeGravacao'

            else:
                if(lista_comandos_e_valores[0] == 'INC'):
                #print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser INCLUIDO é: ", lista_comandos_e_valores[1])





                    try:
                        variavelA = str(lista_comandos_e_valores[1])

                        nova.controledeVersao('INC', str(variavelA))

                        nova.inserirNovoNo(lista_comandos_e_valores[1])
                        print("Tamanho len de A",variavelA)

                    except Exception as err:


                        if  len(lista_comandos_e_valores) == 1:
                            resposta = ' '
                            nova.gerar_log(msg_erro_index, 'INC', resposta, '')
                            exit()
                        resposta = variavelA
                        nova.gerar_log(msg_erro_index,'INC',resposta,'')


                    #nova.gerar_log(msg_erro_index,lista_comandos_e_valores[0],lista_comandos_e_valores[1],'')

                    nova.mostrar_arvore()




                if(lista_comandos_e_valores[0] == 'REM'):

                    try:
                        variavelA = str(lista_comandos_e_valores[1])

                        nova.controledeVersao('REM', str(lista_comandos_e_valores[1]))
                        nova.deletarNo(lista_comandos_e_valores[1])
                    except Exception as err:

                        if len(lista_comandos_e_valores) == 1:
                            resposta = ' '
                            nova.gerar_log(msg_erro_index, 'REM', resposta, '')
                            exit()
                        resposta = variavelA
                        nova.gerar_log(msg_erro_index, 'REM', resposta, '')

                # print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser REMOVIDO é: ", lista_comandos_e_valores[1])




                    #nova.gerar_log(msg_erro_index, lista_comandos_e_valores[0], lista_comandos_e_valores[1], '')

                    nova.mostrar_arvore()
                    print("\n ----- Depois deletar o elemento: ",lista_comandos_e_valores[1])
                    nova.mostrar_arvore()
                  #  self.controle_versao += self.controle_versao

                if (lista_comandos_e_valores[0] == 'IMP'):
                    concatenar_raiz = ''
                    concatenar_antes = ''
                    concatenar_apos = ''
                    concatenar_no01_nivel01 = ''



                    # print("O comando é :", lista_comandos_e_valores[0])
                    #  print(ta"O elemento a ser INCLUID é: ", lista_comandos_e_valores[1],end=' ' )

                    # for i in range(len(lista_comandos_e_valores)):
                    print(type(lista_comandos_e_valores[1]))
                    arqv_saida.write('IMP ')




                    if lista_comandos_e_valores[1] == '0' :
                        msg = "O valor da versão solicitada para impressão IMP é 0," \
                              "\n a primeira versão começa com valor inteiro 1 \n" \
                              "-----------------------------------------------------"
                        nova.gerar_log(msg,'IMP','','0')
                    #    arqv_saida.write(lista_comandos_e_valores[1])
                        arqv_saida.write('\n')
                        exit()
                    else:
                        corrigido = nova.retornar_valor_corrigido()


                        if (int(corrigido) < int(lista_comandos_e_valores[1])):
                            arqv_saida.write(str(corrigido) + ' ')
                            arqv_saida.write('\n')
                            a = nova.retornar_versao(corrigido, False,'')  # valor negativo de IMP não é possivel
                        else:
                            arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                            arqv_saida.write('\n')
                            a = nova.retornar_versao((int(lista_comandos_e_valores[1])), False,'')  # valor negativo de IMP não é possivel
                            controle = True





                        tamanho_vetor_a = len(a)
                        print("Tamanho vetor a antes do for:", tamanho_vetor_a)

                        concatenar_raiz = str(a[0]) + ','
                        concatenar_raiz += str(a[1]) + ','
                        concatenar_raiz += a[2] + ','
                        print("Esta é a raiz: ", concatenar_raiz)
                        if(tamanho_vetor_a <= 4):
                            arqv_saida.write(concatenar_raiz)

                        else:
                            concatenar_antes += str(a[4]) + ','
                            concatenar_antes += str(a[5]) + ','
                            concatenar_antes += a[6] + ','
                            print("Este é o primeiro nó ", concatenar_antes)

      #                          if (lista_comandos_e_valores[1] == '1'):
       #                             arqv_saida.write(concatenar_raiz)
        #                            print("controle antes de 1:", controle)
         #                           controle = False
          #                          print("valor controle depois 1: ",controle)


                          #      if lista_comandos_e_valores[1] == '2':
                           #         arqv_saida.write(concatenar_antes)
                            #        arqv_saida.write(concatenar_raiz)
                             #       print("controle antes de 2:", controle)
                              #      controle = False
                               #     print("valor controle depois 2: ", controle)

                            controle_entrada = False

                            for i in range(8,tamanho_vetor_a,4):
                                print("Valore de i:", i)
                                valor = str(a[i])
                                nivel = str(a[i+1])
                                cor = a[i+2]

                                if (nivel != '1'):
                                    if(controle_entrada == False):
                                        concatenar_antes += valor + ','
                                        concatenar_antes += nivel + ','
                                        concatenar_antes += cor + ','
                                        print("Valore concatenado antes da raiz", concatenar_antes)
                                    ################a ser removio###########
                                    if (controle_entrada == True):
                                        concatenar_apos += valor + ','
                                        concatenar_apos += nivel + ','
                                        concatenar_apos += cor + ','
                                        print("Esta é concaternar depois ", concatenar_apos)
                                    #############a ser removido#################

                                    print("Passou do no 1 do nivel 1", controle_entrada)
                                elif (a[i + 1] == '1') and (controle_entrada == False):
                                    concatenar_no01_nivel01 = valor + ','
                                    concatenar_no01_nivel01 += nivel + ','
                                    concatenar_no01_nivel01 += cor + ','
                                    controle_entrada = True
                                    print("Esta é no 01 do nivel 01 ", concatenar_no01_nivel01)

                        if(tamanho_vetor_a>4):

                            arqv_saida.write(concatenar_antes)
                            arqv_saida.write(concatenar_raiz)
                            arqv_saida.write(concatenar_no01_nivel01)
                            arqv_saida.write(concatenar_apos)


                    arqv_saida.write('\n')



        arqv_saida.close()
if __name__ == "__main__":

    nova = ArvRB()
    #for i in range(21):
    #    nova.inserirNovoNo(i)
    #    nova.mostrar_arvore()

    x = Arquivo('entrada.txt')
    x.lerArquivo()

    x.testeEscrita()


