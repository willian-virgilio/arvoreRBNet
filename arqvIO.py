# from elementosLista import ElementosLista
from array import *

from ArvRB import ArvRB

versao = []
vetor = []
sucessor = []



nova = ArvRB()
class Arquivo:



    def __init__(self,nomeArqv):
        self.nomeArqv = nomeArqv
        self.smsErro = False



    def lerArquivo(self):
        abrir_arquivo = open('entrada.txt', 'r')
        for comando in abrir_arquivo:
            comando = comando.rstrip()
           # print(comando)
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


    def testeEscrita(self):
       # print(self.controle_versao)

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

                print("A versão de busca do sucessor é:", int(lista_comandos_e_valores[2]))
                a = nova.retornar_versao((int(lista_comandos_e_valores[2])),True)
               # if (c >= lista_comandos_e_valores[2] ):
                #    arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                 #   arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                  #  arqv_saida.write(lista_comandos_e_valores[c] + ' ')

               # print("Elementos salvos desta  versão: ",a)
                print("O valor de pesquisa de sucessor: ",int(lista_comandos_e_valores[1]))

                corrigido = nova.retornar_valor_corrigido()
                print("Tipo corrigido: ",type(corrigido))
                print("Valor corrigido: ", corrigido)
                print("Valor da versão solicitada ", lista_comandos_e_valores[2])

                if (int(corrigido) < int(lista_comandos_e_valores[2])):
                    arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                    arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                    arqv_saida.write(str(corrigido) + ' ')
                else:
                    arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                    arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                    arqv_saida.write(lista_comandos_e_valores[2] + ' ')
               # nova.buscar_sucessor(int(lista_comandos_e_valores[1]),int(lista_comandos_e_valores[2]))

                sucessor.clear()

                # if(len(a) == 0)
                for i in range(0,len(a),4):

                    if(int(lista_comandos_e_valores[1]) < int(a[i])):
                        sucessor.append(int(a[i]))
#

                    print("lista de valores de sucessores:", sucessor)
                    print("tamanho", len(sucessor))
                    """
                    por algum motivo estranho a função min() está retornando vazio - ValueError: min() arg is an empty sequence -
                        Porem fazendo os teste a lista esta sendo preenchida com todos os valores acima do de pesquisa de sucessor, 
                        alem do proprio vetor sucessor retornar o tamanho na funcão len(). De tal forma tive que colocar a funcão min() 
                        dentro de um for() que percorre o vetor sucessor dai no final o ultimo valor gravado na variavel x, 
                        acumulando o ultimo valor
                        """
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

                    nova.inserirNovoNo(lista_comandos_e_valores[1])
                    print("Novo No: ", lista_comandos_e_valores[1])
                    nova.mostrar_arvore()




                if(lista_comandos_e_valores[0] == 'REM'):



                # print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser REMOVIDO é: ", lista_comandos_e_valores[1])
                    nova.deletarNo(lista_comandos_e_valores[1])
                    print("\n ----- Depois deletar o elemento: ",lista_comandos_e_valores[1])
                    nova.mostrar_arvore()
                  #  self.controle_versao += self.controle_versao

                if (lista_comandos_e_valores[0] == 'IMP'):
                    concatenar_raiz = ''
                    concatenar_antes = ''
                    concatenar_apos = ''

                    # print("O comando é :", lista_comandos_e_valores[0])
                    #  print("O elemento a ser INCLUID é: ", lista_comandos_e_valores[1],end=' ' )

                    # for i in range(len(lista_comandos_e_valores)):
                    print(type(lista_comandos_e_valores[1]))

                    if lista_comandos_e_valores[1] == '0' :
                        msg = "O valor da versão solicitada para impressão IMP é 0," \
                              "\n a primeira versão começa com valor interio 1"
                        nova.gerar_log(msg)
                        exit()
                    else:
                        controle = True

                        a = nova.retornar_versao((int(lista_comandos_e_valores[1])),False)  # valor negativo de IMP não é possivel

                        concatenar_raiz = a[0] + ','
                        concatenar_raiz += a[1] + ','
                        concatenar_raiz += a[2] + ','
                        print("Esta é a raiz: ", concatenar_raiz)

                        if(len(a)<9) and(len(a)>5):

                            concatenar_antes = a[4] + ','
                            concatenar_antes += a[5] + ','
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
                        print("Tamanho vetor a antes do for:",len(a))
                        for i in range(8,len(a),4):
                            print("Valore de i:", i)
                            valor = a[i]
                            nivel = a[i+1]
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


                        arqv_saida.write(concatenar_antes)
                        arqv_saida.write(concatenar_raiz)
                        arqv_saida.write(concatenar_no01_nivel01)
                        arqv_saida.write(concatenar_apos)


                    arqv_saida.write('\n')



        arqv_saida.close()
