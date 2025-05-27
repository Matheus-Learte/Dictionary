from Grafo import Grafo
import heapq

def LeEntrada(Graft):
    city=None
    city_list = []
    try:
        while True:
            linha = input()

            if linha[0]=='\t':
                aux=linha.strip().split()
                Graft.setNo(city, aux[0], int(aux[1]))
            else:
                city=linha.strip()
                Graft.CreateNo(city)
                city_list.append(city)
    except EOFError:
        pass           
    
    return city_list


def Dijkstra(Graft, origem):
    dist={city: 32000 for city in Graft.getGraft()}
    ordem={city: None for city in Graft.getGraft()}
    dist[origem]=0

    heap = [(0, origem)]

    while heap:
        dist_aresta, aresta = heapq.heappop(heap)

        for neighbor, peso in Graft.getNo(aresta).items():
            new_dist= dist_aresta+peso

            if new_dist<dist[neighbor]:
                dist[neighbor]=new_dist
                ordem[neighbor]=aresta
                heapq.heappush(heap, (new_dist, neighbor))

    return dist, ordem

def Caminho(arestas, origem, destino):
    caminho=[]
    atual = destino

    while atual != None:
        caminho.append(atual)
        atual=arestas[atual]
    caminho.reverse()

    return caminho

graft = Grafo()
city_list=LeEntrada(graft)

for city in city_list:
    cachorro, ordem = Dijkstra(graft, city)

    for i in range(len(city_list)):
        if city_list[i]==city:
            continue
        else:
            print(city+" para "+ city_list[i])
            print("\tDistancia: {:.1f}".format(cachorro[city_list[i]]).replace(".", ","))

            arvore=Caminho(ordem, city, city_list[i])
            caminho = ""
            for atual in arvore:
                if atual == city:
                    continue
                caminho+= " --> "+atual
            
            print("\tCaminho: "+caminho)
    print("-"*45)