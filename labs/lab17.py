# Laboratorio 17 - Banco de Dados Geografico
# Nome: Anne Feng Cai
# RA: 261026
import math
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados) 
#       cep: CEP desejado 
# 
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.   
#
def consulta_cidade_por_cep(cidades, cep):
    i=0
    while i<len(cidades):
        if (cidades[i].inicioCEP<=cep and cidades[i].fimCEP>=cep):
            return i
        i=i+1
    return None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    lista={}; resp=[]; dist=[]
    for i in range(len(cidades)):
        d = distancia(cidades[cidadeReferencia].coordenadas,cidades[i].coordenadas)
        if d<=raio:
            lista[d]= i
    dist=sorted(lista)
    for d in dist:
        resp.append(lista[d])
    return resp

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#          
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    hab=0
    for i in range(len(cidades)): 
        if (distancia(cidades[cidadeReferencia].coordenadas,cidades[i].coordenadas))<=raio:
            hab=hab+cidades[i].numHabitantes
    return hab

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    lista=[]
    for i in range(len(cidades)):
        if (distancia(cidades[cidadeReferencia].coordenadas,cidades[i].coordenadas))<=raio:
            lista.append(cidades[i].numHabitantes)
    lista=sorted(lista)
    if (len(lista)%2==0):
        return (lista[int(len(lista)/2)]+lista[int((len(lista)/2)-1)])/2
    else:
        return lista[int((len(lista)-1)/2)]