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

    def retornaL(self):
        l = []
        pos = self.topo
        while pos != None:
            l.append(pos.pegaDado())
            pos = pos.pegaProx()
        return l[::-1]

    def MostraPlacas(self):
        l = []
        pos = self.topo
        while pos != None:
            l.append(pos.pegaDado()[0])
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

class Estacionamento:
    def __init__(self):
        self.vagasmaximas = 10
        self.pilha=Pilha()
    
    def estacionar(self, vlr):
        if self.pilha.tam() < 10:
            self.pilha.empilhar([vlr, 0])
    
    def retornar(self, vlr):
        if self.pilha.tam() < 10:
            self.pilha.empilhar(vlr)

p = Pilha()    
rua = Pilha()

entrada = input("Placa (precione enter para encerrar sem digitar nada para encerrar): ")
while entrada != "":
    eous = input("S para saída e E para entrada: ")
    while eous != "S" and eous != "E":
        print("Dígite uma entrada valida!")
        eous = input("S para saída e E para entrada: ")
    if eous == "E":
        if entrada in p.MostraPlacas():
            print("Carro já está la dentro")
        elif p.tam() < 10:
            p.empilhar([entrada, 0])
        else:
            print("Sem espaço, carro não entrou!")
    if eous == "S":
        if entrada in p.MostraPlacas():
            while p.topo.dado[0] != entrada:
                mov = p.desempilha()
                mov[1] += 1
                rua.empilhar(mov)
            ret = p.desempilha()
            print(f"carro de placa {ret[0]} saiu do estacionamento e foi manobrado {ret[1]} vez(es) enquanto estava lá!")
            while rua.tam() > 0:
                p.empilhar(rua.desempilha())
        else:
            print("Não está no estacionamento!")
    print(p.MostraPlacas())
    entrada = input("Placa (precione enter para encerrar sem digitar nada para encerrar):")

