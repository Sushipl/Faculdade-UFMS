class Nodo:
    def __init__(self,vlr):
        self.dado = vlr
        self.prox = None
    
    def mudaProx(self, novoProx):
        self.prox = novoProx

    def pegaDado(self):
        return self.dado
    
    def pegaProx(self):
        return self.prox

class Pilha:
    
    def __init__(self):
        self.topo = None

    def estaVazia(self):
        return self.topo == None

    def empilhar(self, vlr):
        temp = Nodo(vlr)
        temp.mudaProx(self.topo)
        self.topo = temp

    def mostra(self):
        pos = self.topo
        while pos != None:
            print(pos.pegaDado(), end=" --> ")
            pos = pos.pegaProx()

    def desempilha(self):
        if self.topo!=None:
            temp = self.topo
            self.topo = self.topo.pegaProx()
            return temp.pegaDado()
        else:
            return self.topo
        
    def tam(self):
        cont = 0
        pos = self.topo
        while pos != None:
            cont +=1
            pos = pos.pegaProx()
        return cont

class Estacionamento:
    def __init__(self):
        self.vagasmaximas = 10
        self.pilha=Pilha()

p = Pilha()
p.empilhar(4)
p.empilhar(7)
print(p.mostra())
