import random
import ctypes
from ArvRB import ArvRB
from arqvIO import Arquivo
from new import AVLTree


if __name__ == "__main__":


    nova = ArvRB()
    x = Arquivo.lerArquivo('entrada')
    print(x)
    Arquivo.testeEscrita('saida')

    nova.inserirNovoNo(70)
    nova.inserirNovoNo(44)
    nova.inserirNovoNo(5)
    nova.inserirNovoNo(4)
    nova.inserirNovoNo(2)
    nova.inserirNovoNo(33)
    nova.inserirNovoNo(18)
    nova.inserirNovoNo(0)
    nova.inserirNovoNo(3)
    nova.inserirNovoNo(78)

    nova.mostrar_arvore()
    nova.imprimir_sucessor()

    print("\n Depois deletar o elemento noVerificado nó")
    nova.deletarNo(44)
    nova.mostrar_arvore()


    print(" ----------- ")

    vetor1 = []
    for i in range(5):
        vetor2 =[]
        #vetor1.append(i + random.randint(1, 9999))
        vetor1.append(vetor2)
        vetor2.append(i + random.randint(1, 9999))
        b = id(vetor1[i])
        vetor2.append(b)
        a = ctypes.cast(vetor1[i][-1], ctypes.py_object).value
        print("valor de a: ",a)
        vetor2.append(a)
        #vertorz.append(ctypes.cast(verto1add[i], ctypes.py_object).value)
    print(vetor1[2][0])

