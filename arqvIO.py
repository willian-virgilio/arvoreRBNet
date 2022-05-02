# from elementosLista import ElementosLista
vetor = []

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


    def testeEscrita(self):
        print("Tamanho do vetor: ",len(vetor))
        escrever_arq = open('saida.txt', 'w')

        for i in range(len(vetor)):
            # O primeiro elemento da lista separador é o comando, o segundo é o valor
            lista_comandos_e_valores = [0]
          #  print("Tamanho da lista inicial: ",len(lista_comandos_e_valores))
            lista_comandos_e_valores = vetor[i].split()
           # print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))


            if( len(lista_comandos_e_valores) > 2):
                print("O sucessor de: "+ lista_comandos_e_valores[1]+ " é: ")
                print("A versão da estrutura é :", lista_comandos_e_valores[2])


            elif(lista_comandos_e_valores == 'INC'):
                print("O comando é :", lista_comandos_e_valores[0])
                print("O elemento a ser inserido é: ", lista_comandos_e_valores[1])

            escrever_arq.write(vetor[i]+' ')
        escrever_arq.close()
        print(vetor)

    def escreverArquivo(self):
        pass



