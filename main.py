import random
import ctypes
from ArvRB import ArvRB
from arqvIO import Arquivo
from new import AVLTree


if __name__ == "__main__":

    nova = ArvRB()
    Arquivo.lerArquivo('entrada')
    try:
        Arquivo.testeEscrita(' ')
    except Exception as err:
        print(err)
       # Arquivo.salvar_erro(" ",err)
        with open('log.txt', 'a') as arqv_log:
            arqv_log.truncate(0)
            arqv_log.write("erro de index, não existe versão nesse indíce informado, "
                           "para buscar o sucessor, por favor corrigir ")
            arqv_log.write('\n')
            arqv_log.close()
            exit()


        print("erro de index, não existe versão nesse indíce informado")
       # Arquivo.smsdeErro('teste',True)

   # nova.inserirNovoNo(70)

    #nova.mostrar_arvore()
    #nova.imprimir_sucessor()

   # nova.deletarNo(44)
   # nova.most if(self.controle_versao == 100):rar_arvore()

    vetor1 = []

    for i in range(5):
        vetor2 = []
        #vetor1.append(i + random.randint(1, 9999))
        vetor1.append(vetor2)
        vetor2.append(i + random.randint(1, 9999))
        b = id(vetor1[i])
        vetor2.append(b)
        a = ctypes.cast(vetor1[i][-1], ctypes.py_object).value
       # print("valor de a: ",a)
        vetor2.append(a)
      #  print(vetor1)




        #vertorz.append(ctypes.cast(verto1add[i], ctypes.py_object).value)





