# from elementosLista import ElementosLista
from array import *
from ArvRB import ArvRB
vetor = []

nova = ArvRB()
class Arquivo:

    def __init__(self,nomeArqv):
        self.nomeArqv = nomeArqv

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

    def testeEscrita(self):
        print("Tamanho do vetor1addr: ",len(vetor))
        arqv_teste = open('teste.txt', 'w')
        arqv_saida = open('saida.txt', 'w')

        for i in range(len(vetor)):
            # O primeiro elemento da lista separador é o comando, o segundo é o valor lista_comandos_e_valores = [0]
            lista_comandos_e_valores = vetor[i].split()

           # print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))

            # primeiro if, caso o vetor1addr tenha indices maior que 2, então ele é o comando SUC de sucessor
            if( len(lista_comandos_e_valores) > 2):
               # print("O sucessor de: "+ lista_comandos_e_valores[1]+ " é: ")
               # print("A versão da estrutura é :", lista_comandos_e_valores[2])
             #   print(lista_comandos_e_valores)
            # verificar erro AttributeError: 'str' object has no attribute 'loopDeGravacao'
            #   self.loopDeGravacao(lista_comandos_e_valores)
                for i in range(len(lista_comandos_e_valores)):
                    a = lista_comandos_e_valores[i]
                    arqv_saida.write(a + ' ')

            else:
                if(lista_comandos_e_valores[0] == 'INC'):
                #print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser INCLUIDO é: ", lista_comandos_e_valores[1])
                    nova.inserirNovoNo(lista_comandos_e_valores[1])
                nova.mostrar_arvore()

                elif(lista_comandos_e_valores[0] == 'REM'):
                # print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser REMOVIDO é: ", lista_comandos_e_valores[1])
                    nova.deletarNo(lista_comandos_e_valores[1])
                    print("\n ----- Depois deletar o elemento: ",lista_comandos_e_valores[1])
                nova.mostrar_arvore()
                elif(lista_comandos_e_valores[0] == 'IMP'):
                # print("O comando é :", lista_comandos_e_valores[0])
                #  print("O elemento a ser INCLUID é: ", lista_comandos_e_valores[1],end=' ' )
                    for i in range(len(lista_comandos_e_valores)):
                        a = lista_comandos_e_valores[i]
                        arqv_saida.write(a + ' ')

            arqv_teste.write(vetor[i]+' ')
        arqv_teste.close()
       # arqv_saida.close()
        print(vetor)

    def escreverArquivo(self):
        pass



