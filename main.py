

from ArvRB import ArvRB
from arqvIO import Arquivo
from new import AVLTree


if __name__ == "__main__":


    nova = ArvRB()
    Arquivo.lerArquivo('entrada')
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
    nova.inserirNovoNo(67)
    nova.inserirNovoNo(65)
    nova.inserirNovoNo(80)
    nova.inserirNovoNo(55)
    nova.inserirNovoNo(45)
    nova.inserirNovoNo(77)
    nova.inserirNovoNo(79)

    nova.mostrar_arvore()
    nova.imprimir_sucessor()

    print("\n Depois deletar o elemento noVerificado nó")
    nova.deletarNo(44)
    nova.mostrar_arvore()



