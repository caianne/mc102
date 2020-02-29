# Nome: Anne Feng Cai; RA: 261026
# Descrição: Funções da biblioteca de conjuntos

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#   num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj:
        return True
    else:
        return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    for i in conj1:
        if (i in conj2)==False:
            return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#    conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if (num in conj)==False:
        conj.append(num)
    return conj

def subtracao(conj, num):
    try:
        conj.remove(num)
    except ValueError:
        return conj
    return conj

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:    # Implementar a funcao e trocar o valor de retorno

#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    l=[]
    for i in conj1:
        l.append(i)
    for i in conj2:
        l.append(i)
    l=set(l)
    return l

def intersecao(conj1, conj2):
    l=[]
    for i in conj1:
        for j in conj2:
            if i==j:
                l.append(i)
                break
    return l

def diferenca(conj1, conj2):
    l=[]
    for i in conj1:
        if (i in conj2)==False:
            l.append(i)
    return l

def uniao_disjunta(conj1, conj2):
    l=[]
    r = uniao(conj1,conj2)
    for i in r:
        if (i in conj1)==False:
            l.append(i)
        if (i in conj2)==False:
            l.append(i)
    l=set(l)
    return l