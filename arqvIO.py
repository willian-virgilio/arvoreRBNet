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
        arqv_teste = open('teste.txt', 'w')
        arqv_saida = open('saida.txt', 'w')

        for i in range(len(vetor)):
            # O primeiro elemento da lista separador é o comando, o segundo é o valor lista_comandos_e_valores = [0]
            lista_comandos_e_valores = vetor[i].split()
           # print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))


            if( len(lista_comandos_e_valores) > 2):
                print("O sucessor de: "+ lista_comandos_e_valores[1]+ " é: ")
                print("A versão da estrutura é :", lista_comandos_e_valores[2])
                for i in range(len(lista_comandos_e_valores)):
                    arqv_saida.write(lista_comandos_e_valores[i] + ' ')
            else:
                if(lista_comandos_e_valores[0] == 'INC'):
                    print("O comando é :", lista_comandos_e_valores[0])
                    print("O elemento a ser INCLUIDO é: ", lista_comandos_e_valores[1])

                if (lista_comandos_e_valores[0] == 'REM'):
                    print("O comando é :", lista_comandos_e_valores[0])
                    print("O elemento a ser REMOVIDO é: ", lista_comandos_e_valores[1])
                if (lista_comandos_e_valores[0] == 'IMP'):
                    print("O comando é :", lista_comandos_e_valores[0])
                    print("O elemento a ser INCLUID é: ", lista_comandos_e_valores[1])


            arqv_teste.write(vetor[i]+' ')
        arqv_teste.close()
        arqv_saida.close()
        print(vetor)

    def escreverArquivo(self):
        pass



