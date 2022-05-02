class No():
    def __init__(self,valor):
        self.valor = valor                                   # Value of Node
        self.antecessor = None                               # Parent of Node
        self.filhoEsquerdo = None                                 # Left Child of Node
        self.filhoDireito = None                                # Right Child of Node
        self.cor = 1                                   # Red Node as new noVerificado is always inserted as Red Node
