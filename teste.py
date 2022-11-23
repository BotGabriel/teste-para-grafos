import string
# Aqui nos temos o algorítmo de Grafos, Vertices, Arestas
class Grafo:
  def __init__ (self, vertices):
    self.vertices = vertices
    self.grafo = [[] for i in range(self.vertices)]

  def adiciona_aresta(self, u, v):
    #grafo não direcionado sem pesos nas arestas
    self.grafo[u-1].append(v)
    self.grafo[v-1].append(u)

  
  def mostra_lista (self):
    for i in range (self.vertices):
      print(f'{i+1}:', end = '  ')
      for j in self.grafo[i]:
        print(f'{j}  ->', end = '  ')
      print('')
# --------------------------------------------------------------------------

# Leitura do arquivo
def loadData(dados):
  with open(dados, "r") as arquivo:
    mensagem = arquivo.readlines()
  return mensagem

#Exemplo de arquivo
l = loadData("C://Users/Leite/Desktop/UFS/Grafos/Trabalho github/fazendo/teste.txt")

# ----------------------------------------------------------------------------

#Split do arquivo em listas das linhas e lista dos vértices
vert = []
lista_linha = []

for i in range(len(l)):
  lista_linha.append(l[i].split())


for i in lista_linha:
  vert.extend(i)

#print("\n")
#print(lista_linha)
#print("\n")
#print(vert)

# Primeira linha informando o número de vértices
n_vert = int(vert[0])
#------------------------------------------------------------------------------

# Manipulação do Grafo e Lista de Adjacências
g = Grafo(n_vert)

x =1

count_arestas = 0

while (x < len(vert)):
  x+=2
  g.adiciona_aresta(int(vert[x-2]), int(vert[x-1]))
  count_arestas += 1

# ------------------------------------------------------------------------------


# Função número de Arestas

def numEdges() -> int:
  return count_arestas

# ------------------------------------------------------------------------------

# Função número de Vertices

def numVertex() -> int:
  return n_vert

#-------------------------------------------------------------------------------

# Busca em Profundidade: Vértice e seus graus

def componentes (lista, vertice):
  i = 1
  lista_aux = []
  marca = 2
  arestas= []
  while (i < len(lista)):
    lista_aux = lista[i]
    if vertice == int(lista_aux[0]) or vertice == int(lista_aux[1]):
      marca = 0
      arestas.append([lista_aux[0], lista_aux[1]])


    i +=1
  if marca == 0:
    return len(arestas), vertice
  else:
    return print("Vertice não encontrado")

#-------------------------------------------------------------------------------

# Busca do grau mínimo

def  minDegree (lista):
  
  x = 1
  lista_extend= []
  lista_grau = []

  for i in lista:
    lista_extend.extend(i)
  
  while (x < len(lista_extend)):

    lista_grau.append(componentes(lista, int(lista_extend[x])))

    x += 2

  lista_grau.sort()

  minGrau = (lista_grau[0])

  return minGrau

#---------------------------------------------------------------------------------

# Busca do grau máximo

def  maxDegree (lista):
  
  x = 1
  lista_extend= []
  lista_grau = []

  for i in lista:
    lista_extend.extend(i)
  
  while (x < len(lista_extend)):

    lista_grau.append(componentes(lista, int(lista_extend[x])))

    x += 2

  lista_grau.sort()

  maxGrau = (lista_grau[len(lista_grau)-1])

  return maxGrau




#---------------------------------------------------------------------------------

#print("\n")
#g.mostra_lista()
print("\n")
print("Numero de Pesquisadores:", numVertex ())
print("\n")
print("Numero de Colaborações:", numEdges())
print("\n")
print("Maior colaboração (quantidade, id):", maxDegree(lista_linha))
print("\n")
print("Menor colaboração: (quantidade, id)", minDegree(lista_linha))
