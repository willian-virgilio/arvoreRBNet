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
    except:

        print("erro de index, não existe versão nesse indíce informado")
       # Arquivo.smsdeErro('teste',True)

   # nova.inserirNovoNo(70)

    #nova.mostrar_arvore()
    #nova.imprimir_sucessor()

   # nova.deletarNo(44)
   # nova.mostrar_arvore()

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





