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
        l = []
        while pos != None:
            l.append(pos.pegaDado())
            pos = pos.pegaProx()
        return l[::-1]

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

p = Pilha()
inp = input()
for letra in inp:
    if letra == "(" or letra ==")":
        p.empilhar(letra)

certo = True
abre = 0
for i in p.mostra():

    if i == "(":
        abre+=1
    elif i == ")":
        abre-=1
    if abre < 0:
        certo = False
if abre != 0:
    certo = False
if certo:
    print("correto")
else:
    print("incorreto")