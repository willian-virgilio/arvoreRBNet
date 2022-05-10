import ctypes
import random

from No import No


class ArvRB():


    def __init__(self):
        self.NULL = No (0)
        self.NULL.cor = 0
        self.NULL.filhoEsquerdo = None
        self.NULL.filhoDireito = None
        self.raiz = self.NULL
        self.sucessor = 0
        self.contadorx = 0
        self.valor_no = None
        self.cor = None
        self.nivel = None
        self.z = ''
        self.y = ''
        self.vetor_grava_versao2 = []
        self.vetor_grava_versao1 = []
        self.vetor_concatenador = []
        self.controle_versao = 0
        self.corrigido = 0
        self.lado = None


    def __gravar_versao(self,valor,nivel,cor,lado):

      # for i in range(nivel):
            #vetor_grava_versao1 = []

        self.y = "%s;%s;%s;"%(valor,nivel,cor)
        self.z += self.y
        self.vetor_grava_versao1.append(valor)
        self.vetor_grava_versao1.append(str(nivel))
        self.vetor_grava_versao1.append(cor)
        self.vetor_grava_versao1.append(lado)




            #vetor_grava_versao2.append(vetor_grava_versao1)

            #vetor_grava_versao2.append(vetor_grava_versao1)
            #print("O vetor completo é: ",vetor_grava_versao2)
           # x = vetor_grava_versao1[-1]
            #print("Espaço de memoria:", x)
           # a = ctypes.cast(x, ctypes.py_object).value
           # print("valor armazenado no espaço de memoria: ", a)
           # print("VEtor 2d ultimo vetor inserido: ", vetor_grava_versao2[-1])
           # print("VEtor 2d ultimo elemento inserido: ", vetor_grava_versao2[i][0])
           # print("VEtor 2d endereço de memoria do ultimo elemento: ", vetor_grava_versao2[i][1])

    # Insert New Node
    def controledeVersao(self):
        self.controle_versao = self.controle_versao + 1
        print("numero de versão: ",self.controle_versao)
        if(self.controle_versao >= 100):
            print("O numero de versões alcançou o limite de 100!.\n O arquivo entrada.txt"
                  " contem mais de 100 operacções de modificação( INC = incluir; REM = Remoção"
                  "\n revise o arquivo de entrada para reduzir a quantidade de Elementos inclusos ou removidos")
            with open('log.txt', 'a') as arqv_log:
                arqv_log.truncate(0)
                arqv_log.write("O numero de versões alcançou o limite de 100!.\n O arquivo entrada.txt"
                  " contem mais de 100 operacções de modificação( INC = incluir; REM = Remoção"
                  "\n revise o arquivo de entrada para reduzir a quantidade de Elementos inclusos ou removidos")
                arqv_log.write('\n')
                arqv_log.close()
            exit()

    def inserirNovoNo(self, key1):
        self.controledeVersao()

        no = No(key1)
        no.antecessor = None
        no.valor = key1
        no.filhoEsquerdo = self.NULL
        no.filhoDireito = self.NULL
        no.cor = 1                                   # Set raiz colour as Red

        v1 = None
        v2 = self.raiz

        while v2 != self.NULL :                           # Find position for new noVerificado
            v1 = v2
            if no.valor < v2.valor :
                v2 = v2.filhoEsquerdo
            else :
                v2 = v2.filhoDireito

        no.antecessor = v1                                  # Set antecessor of Node as y
        if v1 == None :                                   # If antecessor i.e, is none then it is raiz noVerificado
            self.raiz = no
        elif no.valor < v1.valor :                          # Check if it is filhoDireito Node or Left Node by checking the value
            v1.filhoEsquerdo = no
        else :
            v1.filhoDireito = no

        if no.antecessor == None :                         # Root noVerificado is always Black
            no.cor = 0
            return

        if no.antecessor.antecessor == None :                  # If antecessor of noVerificado is Root Node
            return

        self.rotacionarInsercao (no)                          # Else call for Fix Up


    def minimo(self, no):
        while no.filhoEsquerdo != self.NULL:
            no = no.filhoEsquerdo
        return no


    # Code for filhoEsquerdo rotate
    def rotacaoParaEsquerda (self, key2) :
        v3 = key2.filhoDireito                                      # Y = Right child of key2
        key2.filhoDireito = v3.filhoEsquerdo                                 # Change filhoDireito child of key2 to filhoEsquerdo child of y
        if v3.filhoEsquerdo != self.NULL :
            v3.filhoEsquerdo.antecessor = key2

        v3.antecessor = key2.antecessor                              # Change antecessor of y as antecessor of key2
        if key2.antecessor == None :                            # If antecessor of key2 == None ie. raiz noVerificado
            self.raiz = v3                                # Set y as raiz
        elif key2 == key2.antecessor.filhoEsquerdo :
            key2.antecessor.filhoEsquerdo = v3
        else :
            key2.antecessor.filhoDireito = v3
        v3.filhoEsquerdo = key2
        key2.antecessor = v3


    # Code for filhoDireito rotate
    def rotacaoParaDireita (self, key3) :
        v5 = key3.filhoEsquerdo                                       # Y = Left child of key2
        key3.filhoEsquerdo = v5.filhoDireito                                 # Change filhoEsquerdo child of key2 to filhoDireito child of y
        if v5.filhoDireito != self.NULL :
            v5.filhoDireito.antecessor = key3

        v5.antecessor = key3.antecessor                              # Change antecessor of y as antecessor of key2
        if key3.antecessor == None :                            # If key2 is raiz noVerificado
            self.raiz = v5                                # Set y as raiz
        elif key3 == key3.antecessor.filhoDireito :
            key3.antecessor.filhoDireito = v5
        else :
            key3.antecessor.filhoEsquerdo = v5
        v5.filhoDireito = key3
        key3.antecessor = v5


    # Fix Up Insertion
    def rotacionarInsercao(self, key4):
        while key4.antecessor.cor == 1:                        # While antecessor is red
            if key4.antecessor == key4.antecessor.antecessor.filhoDireito:         # if antecessor is filhoDireito child of its antecessor
                v6 = key4.antecessor.antecessor.filhoEsquerdo                  # Left child of grandparent
                if v6.cor == 1:                          # if cor of filhoEsquerdo child of grandparent i.e, uncle noVerificado is red
                    v6.cor = 0                           # Set both children of grandparent noVerificado as black
                    key4.antecessor.cor = 0
                    key4.antecessor.antecessor.cor = 1             # Set grandparent noVerificado as Red
                    key4 = key4.antecessor.antecessor                   # Repeat the algo with Parent noVerificado to check conflicts
                else:
                    if key4 == key4.antecessor.filhoEsquerdo:                # If key4 is filhoEsquerdo child of it's antecessor
                        key4 = key4.antecessor
                        self.rotacaoParaDireita(key4)                        # Call for filhoDireito rotation
                    key4.antecessor.cor = 0
                    key4.antecessor.antecessor.cor = 1
                    self.rotacaoParaEsquerda(key4.antecessor.antecessor)
            else:                                         # if antecessor is filhoEsquerdo child of its antecessor
                v6 = key4.antecessor.antecessor.filhoDireito                 # Right child of grandparent
                if v6.cor == 1:                          # if cor of filhoDireito child of grandparent i.e, uncle noVerificado is red
                    v6.cor = 0                           # Set cor of childs as black
                    key4.antecessor.cor = 0
                    key4.antecessor.antecessor.cor = 1             # set cor of grandparent as Red
                    key4 = key4.antecessor.antecessor                   # Repeat algo on grandparent to remove conflicts
                else:
                    if key4 == key4.antecessor.filhoDireito:               # if key4 is filhoDireito child of its antecessor
                        key4 = key4.antecessor
                        self.rotacaoParaEsquerda(key4)                        # Call filhoEsquerdo rotate on antecessor of key4
                    key4.antecessor.cor = 0
                    key4.antecessor.antecessor.cor = 1
                    self.rotacaoParaDireita(key4.antecessor.antecessor)              # Call filhoDireito rotate on grandparent
            if key4 == self.raiz:                            # If key4 reaches raiz then break
                break
        self.raiz.cor = 0                               # Set cor of raiz as black


    # Function to fix issues after deletion
    def ajustarAposDeletar (self, key5) :
        while key5 != self.raiz and key5.cor == 0 :           # Repeat until key2 reaches nodes and cor of key2 is black
            if key5 == key5.antecessor.filhoEsquerdo :                       # If key2 is filhoEsquerdo child of its antecessor
                v7 = key5.antecessor.filhoDireito                        # Sibling of key2
                if v7.cor == 1 :                         # if sibling is red
                    v7.cor = 0                           # Set its cor to black
                    key5.antecessor.cor = 1                    # Make its antecessor red
                    self.rotacaoParaEsquerda (key5.antecessor)                  # Call for filhoEsquerdo rotate on antecessor of key2
                    v7 = key5.antecessor.filhoDireito
                # If both the child are black
                if v7.filhoEsquerdo.cor == 0 and v7.filhoDireito.cor == 0 :
                    v7.cor = 1                           # Set cor of s as red
                    key5 = key5.antecessor
                else :
                    if v7.filhoDireito.cor == 0 :               # If filhoDireito child of s is black
                        v7.filhoEsquerdo.cor = 0                  # set filhoEsquerdo child of s as black
                        v7.cor = 1                       # set cor of s as red
                        self.rotacaoParaDireita (v7)                     # call filhoDireito rotation on key2
                        v7 = key5.antecessor.filhoDireito

                    v7.cor = key5.antecessor.cor
                    key5.antecessor.cor = 0                    # Set antecessor of key2 as black
                    v7.filhoDireito.cor = 0
                    self.rotacaoParaEsquerda (key5.antecessor)                  # call filhoEsquerdo rotation on antecessor of key2
                    key5 = self.raiz
            else :                                        # If key2 is filhoDireito child of its antecessor
                v7 = key5.antecessor.filhoEsquerdo                         # Sibling of key2
                if v7.cor == 1 :                         # if sibling is red
                    v7.cor = 0                           # Set its cor to black
                    key5.antecessor.cor = 1                    # Make its antecessor red
                    self.rotacaoParaDireita (key5.antecessor)                  # Call for filhoDireito rotate on antecessor of key2
                    v7 = key5.antecessor.filhoEsquerdo

                if v7.filhoDireito.cor == 0 and v7.filhoDireito.cor == 0 :
                    v7.cor = 1
                    key5 = key5.antecessor
                else :
                    if v7.filhoEsquerdo.cor == 0 :                # If filhoEsquerdo child of s is black
                        v7.filhoDireito.cor = 0                 # set filhoDireito child of s as black
                        v7.cor = 1
                        self.rotacaoParaEsquerda (v7)                     # call filhoEsquerdo rotation on key2
                        v7 = key5.antecessor.filhoEsquerdo

                    v7.cor = key5.antecessor.cor
                    key5.antecessor.cor = 0
                    v7.filhoEsquerdo.cor = 0
                    self.rotacaoParaDireita (key5.antecessor)
                    key5 = self.raiz

        key5.cor = 0



    # Function to transplant nodes
    def __transposicao_rb (self, v8, key6) :
        if v8.antecessor == None :
            self.raiz = key6
        elif v8 == v8.antecessor.filhoEsquerdo :
            v8.antecessor.filhoEsquerdo = key6
        else :
            v8.antecessor.filhoDireito = key6
        key6.antecessor = v8.antecessor


    # Function to handle deletion
    def __auxDel_no (self, no, key7) :
        v9 = self.NULL
        while no != self.NULL :                          # Search for the noVerificado having that value/ key1 and store it in 'v9'
            if no.valor == key7 :
                v9 = no

            if no.valor <= key7 :
                no = no.filhoDireito

            else :
                no = no.filhoEsquerdo



        if v9 == self.NULL :                                # If Kwy is not present then deletion not possible so return
            print ( "O elemento não esta presente na arvore" )
            return

        v10 = v9
        v10_cor_anterior = v10.cor                          # Store the cor of v9- noVerificado
        if v9.filhoEsquerdo == self.NULL :                            # If filhoEsquerdo child of v9 is NULL
            v11 = v9.filhoDireito                                     # Assign filhoDireito child of v9 to key2
            self.__transposicao_rb (v9, v9.filhoDireito)            # Transplant Node to be deleted with key2
        elif (v9.filhoDireito == self.NULL) :                       # If filhoDireito child of v9 is NULL
            v11 = v9.filhoEsquerdo                                      # Assign filhoEsquerdo child of v9 to key2
            self.__transposicao_rb (v9, v9.filhoEsquerdo)             # Transplant Node to be deleted with key2
        else :                                              # If v9 has both the child nodes
            v10 = self.minimo (v9.filhoDireito)                    # Find minimum of the filhoDireito sub tree
            v10_cor_anterior = v10.cor                      # Store cor of y
            v11 = v10.filhoDireito
            if v10.antecessor == v9 :                              # If y is child of v9
                v11.antecessor = v10                                # Set antecessor of key2 as y
            else :
                self.__transposicao_rb (v10, v10.filhoDireito)
                v10.filhoDireito = v9.filhoDireito
                v10.filhoDireito.antecessor = v10

            self.__transposicao_rb (v9, v10)
            v10.filhoEsquerdo = v9.filhoEsquerdo
            v10.filhoEsquerdo.antecessor = v10
            v10.cor = v9.cor
        if v10_cor_anterior == 0 :                          # If cor is black then fixing is needed
            self.ajustarAposDeletar (v11)


    # Deletion of noVerificado
    def deletarNo (self, valor) :
        self.controledeVersao()
        self.__auxDel_no (self.raiz, valor)         # Call for deletion


    # Function to print
    def __mostrar (self, noVerificado, identador, final,e_raiz,contadory) :
    #def __mostrar(self, noVerificado, identador, final):

        if noVerificado != self.NULL :
            s_cor = "R" if noVerificado.cor == 1 else "N" # R = Rubro e N = Negro

            print(identador, end=' ')
            if e_raiz :
                self.contadorx = 0
                contadory = 0
                print("Nivel %s - Raiz:::" %(contadory),end=' ')
                identador += "     "
                e_raiz = False
                noVerificadoAnterior = noVerificado.valor
                contadoryAnterior = contadory
                s_corAnterior = s_cor
                self.z = ''
                self.y = ''
                lado = "raiz"

                if((noVerificadoAnterior != noVerificado) and (contadoryAnterior != contadory) and (s_corAnterior != s_cor)):
                   self.__gravar_versao(noVerificado.valor,contadory,s_cor,lado)


            #    z = '%s %s %s'%(noVerificado.valor,contadory,s_cor)
             #   vetor_grava_versao1.append(z)
                self.contadorx = self.contadorx + 1
               # self.imprimir_sucessor()
            else:
                if final:
                    print ("Nivel %s - DIREITA----"%(contadory),end=' ')
                    identador += "     "
                    lado = "dir"

                else :
                    print("Nivel %s - ESQUERDA----"%(contadory),end=' ')
                    identador += "|    "
                    lado = "esq"
            print (str (noVerificado.valor) + "(" + s_cor + ")")


            self.__gravar_versao(noVerificado.valor, contadory, s_cor,lado)



            #print("Novo No: ", self.imprimir_sucessor())

          #  self.__mostrar (noVerificado.filhoEsquerdo, identador, False)
            self.__mostrar(noVerificado.filhoEsquerdo, identador, False, False,contadory = contadory+1)

          #  v1 = str(noVerificado.filhoEsquerdo).split()


           # print("Valor: ",ctypes.cast(140148353592000,ctypes.py_object).value)
            self.__mostrar (noVerificado.filhoDireito, identador, True,False,contadory = contadory+1)

    def retornar_valor_corrigido(self):
        return int(self.corrigido)

    def retornar_versao(self, index,e_sucessor=False):


        print("Numero do indice do vetor da versão existente: ", index)

        if index == -1:
            print("O valor da versão solicitada para impressão IMP é 0,"
                  "\n a primeira versão começa com valor interio 1")
            exit()

        print("o valor do indice do vetor grava versão 2 , na função retornar versão é:", index)
        print("O tamanho do vetor grava versão 2 é: ", len(self.vetor_grava_versao2))



        try:
            a = self.vetor_grava_versao2[index]
        except Exception as err:

            print(err)
            if(e_sucessor==True):
                if(index <= len(self.vetor_grava_versao2)):
                    a = self.vetor_grava_versao2[index]

                    return a
                    exit()
                else:
                    self.corrigido = len(self.vetor_grava_versao2)
                    print("valor corrigido: ",self.corrigido)
                    a = self.vetor_grava_versao2[self.corrigido-1]
                    with open('log.txt', 'a') as arqv_log:
                        arqv_log.truncate(0)
                        arqv_log.write("Alerta: A versão solicitada para ser mostrada ainda é maior,\n "
                                       "que a ultima versão gravada, portanto \n"
                                       "sera mostrado o sucessor nó solicitado , da ultima\n"
                                       "versão gravada " )
                        arqv_log.write('\n')
                        arqv_log.close()
                    print("Alerta: A versão solicitada para ser mostrada ainda é maior,\n "
                                       "que a ultima versão gravada, portanto \n"
                                       "sera mostrado o sucessor nó solicitado , da ultima\n"
                                       "versão gravada ")
                    self.retornar_valor_corrigido()
                    return a
                    #return a
                    exit()
            else:
                with open('log.txt', 'a') as arqv_log:
                    arqv_log.truncate(0)
                    arqv_log.write("A versão solicitada para ser mostrada ainda não existe,\n "
                    "Por favor corrigir, para continuar")
                    arqv_log.write('\n')
                    arqv_log.close()
                print("A versão solicitada para ser mostrada ainda não existe,\n "
                  "Por favor corrigir, para continuar")
                exit()
        return a
    # Function to call print
    def mostrar_arvore (self) :

        self.__mostrar (self.raiz,"",True,True,0)


        print(self.z)


       # print(self.vetor_grava_versao1)
        s = len(self.vetor_grava_versao1)



        self.vetor_grava_versao2.append(self.vetor_grava_versao1)
        self.vetor_grava_versao1 = []

        for i in range(len(self.vetor_grava_versao2)):

                print(self.vetor_grava_versao2[i])
        print(self.vetor_grava_versao2)



       # vetor_grava_versao1.append(self.z)
      #  d = str(vetor_grava_versao1).split(';')
       # print(d,end='\n')

       # self.__mostrar (self.raiz, "", True)


    def buscar_sucessor(self,antecessor,versao):
        pass


