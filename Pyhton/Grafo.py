class Grafo():
    def __init__(self):
        self.nos={}
    
    def getNo(self, nome):
        return self.nos[nome]

    def printNos(self):
        print(self.nos)
    
    def CreateNo(self, nome):
        self.nos[nome]= {}

    def getGraft(self):
        return list(self.nos.keys())

    def setNo(self, nome, aux, dist):
        self.nos[nome][aux]=dist
    
    def EraseNo(self, nome, aux):
        return self.nos.pop(nome)