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

    vertorx = []
    vertory = []
    vertorz = []
    for i in range(10):
        vertorx.append(i + random.randint(1,9999))
        vertory.append(id(vertorx[i]))
        vertorz.append(ctypes.cast(vertory[i], ctypes.py_object).value)
    print(vertorx)
    print(vertory)
    print(vertorz)


