
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
        self.concatenar_antes = ''
        self.concatenar_apos = ''
        self.concatenar_no01_nivel01 = ''
        self.stringConcatenadaSUC = ''


    def getStringRaizCentro(self):
        pass


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

    def get_stringConcate(self):
        return self.stringConcatenadaSUC

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


    def testeEscrita(self,e_sucessor=False,num_versao=0):
#        print(self.controle_versao)
        msg_erro_index = "Erro : Valor a ser inserido ou removido é inexistente, \n" \
                         "ou a operação  contem algum caracter invalido" \
                        "O arquivo entrada.txt contem uma instrução invalida, \n " \
                        "Verifique as seguntes possibilidades:\n" \
                        " 1 - Se alguma instrução esta faltando numero posterior a ela. \n" \
                        "Exemplo: INC  <-----está sem o numero da versão!!\n" \
                        "    2 - Se contem caracter invalido, não numerico.: Exemplo REM x \n"
        if (e_sucessor == True):
            vetortemp = []
            vetortemp.append('IMP')
            vetortemp.append(str(num_versao))
            tam_vet = len(vetortemp)
            print("Valor da lista tam_vetor", vetortemp)
        else:
            print("Tamanho do vetor1: ",len(vetor))
            tam_vet = len(vetor)
            arqv_saida = open('saida.txt', 'a')
            arqv_saida.truncate(0)


        lista_comandos_e_valores = []
        lista_comandos_e_valores_SUC = []



        for i in range(0,tam_vet,1):


            # O primeiro elemento da lista separador é o comando, o segundo é o valor lista_comandos_e_valores = [0]
            if(e_sucessor == True):
                lista_comandos_e_valores = vetortemp
                print("Valor da lista, caso e_sucessor = True:",lista_comandos_e_valores)
            else:
                lista_comandos_e_valores = vetor[i].split()
                print("toda a lista :",lista_comandos_e_valores)
                print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))

            # primeiro if, caso o vetor1addr tenha indices maior que 2, então ele é o comando SUC de sucessor
            if( len(lista_comandos_e_valores) > 2):
                print("O sucessor de: "+ lista_comandos_e_valores[1]+ " é: ")
                print("A versão da estrutura é :", lista_comandos_e_valores[2])
                print(lista_comandos_e_valores)
                nversao = (int(lista_comandos_e_valores[2]))
                print("A versão de busca do sucessor é:", nversao)
                elemento = int(lista_comandos_e_valores[1])

                a = nova.retornar_versao(nversao,True,elemento)
               # if (c >= lista_comandos_e_valores[2] ):
                #    arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                 #   arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                  #  arqv_saida.write(lista_comandos_e_valores[c] + ' ')

                print("Elementos salvos desta  versão: ",a)
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
                    x = int(lista_comandos_e_valores[1])
                    y = int(a[i])

                    if( x < y ):

                        sucessor.append(y)

                        zy = self.testeEscrita(True, 11)
                        print("valor apos executar testeEscrita em SUC:", zy)

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

                        nova.controledeVersao('INC', lista_comandos_e_valores[1])

                        nova.inserirNovoNo(int(lista_comandos_e_valores[1]))

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


                        nova.controledeVersao('REM', lista_comandos_e_valores[1])

                        nova.deletarNo(int(lista_comandos_e_valores[1]))
                    except Exception as err:

                        if len(lista_comandos_e_valores) == 1:
                            resposta = ' '
                            nova.gerar_log(msg_erro_index, 'REM', resposta, '')
                            exit()
                        resposta = variavelA
                        nova.gerar_log(msg_erro_index, 'REM', resposta, '')

                    print("O comando é :", lista_comandos_e_valores[0])
                    print("O elemento a ser REMOVIDO é: ", lista_comandos_e_valores[1])




                    #nova.gerar_log(msg_erro_index, lista_comandos_e_valores[0], lista_comandos_e_valores[1], '')

                    nova.mostrar_arvore()
                    print("\n ----- Depois deletar o elemento: ",lista_comandos_e_valores[1])
                    nova.mostrar_arvore()
                  #  self.controle_versao += self.controle_versao

                if (lista_comandos_e_valores[0] == 'IMP'):
                    self.concatenar_raiz = ''
                    self.concatenar_antes = ''
                    self.concatenar_apos = ''
                    self.concatenar_no01_nivel01 = ''
                    self.concatenar_raiz = ''



                    print("O comando é :", lista_comandos_e_valores[0])
                    #  print(ta"O elemento a ser INCLUID é: ", lista_comandos_e_valores[1],end=' ' )

                    # for i in range(len(lista_comandos_e_valores)):
                    print(type(lista_comandos_e_valores[1]))





                    if lista_comandos_e_valores[1] == '0' :
                            msg = "O valor da versão solicitada para impressão IMP é 0," \
                                  "\n a primeira versão começa com valor inteiro 1 \n" \
                                  "-----------------------------------------------------"
                            nova.gerar_log(msg,'IMP','','0')
                        #    arqv_saida.write(lista_comandos_e_valores[1])
                            if (e_sucessor == False):
                                arqv_saida.write('\n')
                                exit()
                            else:
                                exit()
                    else:
                            corrigido = nova.retornar_valor_corrigido()


                            if (int(corrigido) < int(lista_comandos_e_valores[1])):
                                if (e_sucessor == False):
                                    arqv_saida.write('IMP ')
                                    arqv_saida.write(str(corrigido) + ' ')
                                    arqv_saida.write('\n')
                                    msg = "Alerta: A versão solicitada para ser mostrada ainda é maior,\n " \
                                          "que a ultima versão gravada,portanto sera mostrado\n" \
                                          " a arvore  da ultima versão gravada \n" \
                                          "----------------------------------------------------------"
                                    nova.gerar_log(msg, 'IMP', '', lista_comandos_e_valores[1])

                                a = nova.retornar_versao(corrigido, False,lista_comandos_e_valores[1])  # valor negativo de IMP não é possivel
                            else:
                                if (e_sucessor == False):
                                    arqv_saida.write('IMP ')
                                    arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                                    arqv_saida.write('\n')
                                a = nova.retornar_versao((int(lista_comandos_e_valores[1])), False,lista_comandos_e_valores[1])  # valor negativo de IMP não é possivel
                                controle = True





                            tamanho_vetor_a = len(a)
                            print("Tamanho vetor a antes do for:", tamanho_vetor_a)

                            self.concatenar_raiz = str(a[0]) + ','
                            self.concatenar_raiz += str(a[1]) + ','
                            self.concatenar_raiz += a[2] + ','
                            print("Esta é a raiz: ", self.concatenar_raiz)
                            if(tamanho_vetor_a <= 4):
                                if (e_sucessor == False):
                                    arqv_saida.write(self.concatenar_raiz)

                                else:
                                    self.stringConcatenadaSUC = self.concatenar_raiz
                                    print("Valor concaternado da self.stringConcatenadaSUC\n"
                                      "se o vetor for menor que 4 : %s" % self.stringConcatenadaSUC)
                                    return self.get_stringConcate()


                            else:
                                self.concatenar_antes += str(a[4]) + ','
                                self.concatenar_antes += str(a[5]) + ','
                                self.concatenar_antes += a[6] + ','
                                print("Este é o primeiro nó ", self.concatenar_antes)

          #                          if (lista_comandos_e_valores[1] == '1'):
           #                             arqv_saida.write(self.concatenar_raiz)
            #                            print("controle antes de 1:", controle)
             #                           controle = False
              #                          print("valor controle depois 1: ",controle)


                              #      if lista_comandos_e_valores[1] == '2':
                               #         arqv_saida.write(self.concatenar_antes)
                                #        arqv_saida.write(self.concatenar_raiz)
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
                                            self.concatenar_antes += valor + ','
                                            self.concatenar_antes += nivel + ','
                                            self.concatenar_antes += cor + ','
                                            print("Valore concatenado antes da raiz", self.concatenar_antes)
                                        ################a ser removio###########
                                        if (controle_entrada == True):
                                            self.concatenar_apos += valor + ','
                                            self.concatenar_apos += nivel + ','
                                            self.concatenar_apos += cor + ','
                                            print("Esta é concaternar depois ", self.concatenar_apos)
                                        #############a ser removido#################

                                        print("Passou do no 1 do nivel 1", controle_entrada)
                                    elif (a[i + 1] == '1') and (controle_entrada == False):
                                        self.concatenar_no01_nivel01 = valor + ','
                                        self.concatenar_no01_nivel01 += nivel + ','
                                        self.concatenar_no01_nivel01 += cor + ','
                                        controle_entrada = True
                                        print("Esta é no 01 do nivel 01 ", self.concatenar_no01_nivel01)

                            if(tamanho_vetor_a>4):

                                if (e_sucessor == False):
                                    arqv_saida.write(self.concatenar_antes)
                                    arqv_saida.write(self.concatenar_raiz)
                                    arqv_saida.write(self.concatenar_no01_nivel01)
                                    arqv_saida.write(self.concatenar_apos)
                                elif (e_sucessor == True):
                                    self.stringConcatenadaSUC = self.concatenar_antes
                                    self.stringConcatenadaSUC += self.concatenar_raiz
                                    self.stringConcatenadaSUC += self.concatenar_no01_nivel01
                                    self.stringConcatenadaSUC += self.concatenar_apos
                                    print("Valor concaternado da self.stringConcatenadaSUC\n"
                                          "se o vetor for maior que 4 :", self.stringConcatenadaSUC)
                                    return self.get_stringConcate()






                    if (e_sucessor == False):
                        arqv_saida.write('\n')


        if (e_sucessor == False):
            arqv_saida.close()


if __name__ == "__main__":

    nova = ArvRB()
    #for i in range(21):
    #    nova.inserirNovoNo(i)
    #    nova.mostrar_arvore()

    x = Arquivo('entrada.txt')
    x.lerArquivo()
    x.testeEscrita(False,0)
   # zy = x.testeEscrita(True, 1)
  #  print("valor apos executar testeEscrita em SUC:")
  #  print("valor apos executar testeEscrita em SUC:", zy)


