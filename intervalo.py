class Intervalo:
    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin

    # Metodos de acceso

def getInicio(self):
    return self.inicio
def getFin(self):
    return self.fin

def escribirIntervalo(self):
    print("\nInicio: "+self.getInicio()+"\nFin: "+self.getFin())

def antes(self, otro):
    return self.getInicio() < otro.getInicio()

def antes(self, otro):
    return not antes(self, otro)

def igual(self, otro):
    return self.getInicio() == otro.getInicio() and self.getFinal() == otro.getFinal()

def encuentra(self, otro):
    return otro.getInicio() == self.getFinal()

def solapa(self, otro):
    return self.getInicio() < otro.getInicio() and self.getFinal() < otro.getFinal()

def solapaI(self, otro):
    return self.getInicio() > otro.getInicio() and self.getFinal() > otro.getFinal()

def durante(self, otro):
    return self.getInicio() > otro.getInicio() and self.getFinal() < otro.getFinal()

def duranteI(self, otro):
    return self.getInicio() < otro.getInicio() and self.getFinal() > otro.getFinal()

def comienza(self, otro):
    return self.getInicio() == otro.getInicio()

def comienzaI(self, otro):
    return not comienza(self, otro)

def finaliza(self, otro):
    return self.getFinal() == otro.getFinal()

def finalizaI(self, otro):
    return not finaliza(self, otro)
