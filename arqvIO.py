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
        arqv_saida = open('saida.txt', 'w')


        for i in range(len(vetor)):

            # O primeiro elemento da lista separador é o comando, o segundo é o valor lista_comandos_e_valores = [0]
            lista_comandos_e_valores = vetor[i].split()
           # print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))

            # primeiro if, caso o vetor1addr tenha indices maior que 2, então ele é o comando SUC de sucessor
            if( len(lista_comandos_e_valores) > 2):
              #  print("O sucessor de: "+ lista_comandos_e_valores[1]+ " é: ")
              #  print("A versão da estrutura é :", lista_comandos_e_valores[2])
                #print(lista_comandos_e_valores)

                print("A versão de busca do sucessor é:", int(lista_comandos_e_valores[2]))
                a = nova.retornar_versao((int(lista_comandos_e_valores[2]) - 1),True)
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



                if(lista_comandos_e_valores[0] == 'IMP'):
                    concatenar_a_direita = ''
                    concatenar_a_esquerda = ''
                    concatenar_raiz = ''
                    indice = 0

                # print("O comando é :", lista_comandos_e_valores[0])
                #  print("O elemento a ser INCLUID é: ", lista_comandos_e_valores[1],end=' ' )

                    #for i in range(len(lista_comandos_e_valores)):
                    print(type(lista_comandos_e_valores[1]))
                    print(type(int(lista_comandos_e_valores[1])))


                    a = nova.retornar_versao((int(lista_comandos_e_valores[1]) - 1),False) # valor negativo de IMP não é possivel
                    print("Vetor A: ",a)

                    ifend = 3
                    ant = None
                    if (int(a[1]) == 0):  # GRava valores da raiz
                        concatenar_raiz = (a[0] + ',')
                        concatenar_raiz += (a[1] + ',')
                        concatenar_raiz += (a[2] + ',')

                        imp_raiz = True


                    if (int(a[5]) == 1):

                        concatenar_no01_direita = (a[4] + ',')
                        concatenar_no01_direita += (a[5] + ',')
                        concatenar_no01_direita += (a[6] + ',')



                    print("tamanho do vetor:",len(a))
                    for i in range(9,len(a),4):
                        print("valor de i:" ,i)
                        print("Tipo da nivel: " ,type(a[i]))
                        print("valor do nivel:", a[i])
                        print("valor anterior ao nivel",a[i-1])

                        if (a[i] == '1'):
                            indice = i
                            break
                        concatenar_a_direita += (a[i - 1] + ',')
                        concatenar_a_direita += (a[i] + ',')
                        concatenar_a_direita += (a[i + 1] + ',')

                    print("a raiz é essa:", concatenar_raiz)
                    print("Este é o primeiro nó:", concatenar_no01_direita)




                    print("Valor da concatenação a direita: ", concatenar_a_direita)
                    print("Valor do indice para o segundo for:", indice)
                    for i in range(indice, len(a), 4):

                        print("Valor do i segundo for:", i)
                        concatenar_a_esquerda+= (a[i - 1] + ',')
                        concatenar_a_esquerda += (a[i] + ',')
                        concatenar_a_esquerda += (a[i + 1] + ',')

                    print("Valor da concatenação a esqueda: ", concatenar_a_esquerda)
                    arqv_saida.write(concatenar_a_direita)
                    arqv_saida.write(concatenar_no01_direita)
                    arqv_saida.write(concatenar_raiz)
                    arqv_saida.write(concatenar_a_esquerda)
                    arqv_saida.write('\n')
        arqv_saida.close()
