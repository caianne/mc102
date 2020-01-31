#Slide 21 da Aula 22
def soma(mat1,mat2):
    try:
        matsoma=[[mat1[i][j]+mat2[i][j] for j in range(len(mat1[i]))] for i in range(len(mat1))]
        return matsoma
    except IndexError as msg:
        print(msg)

def mult(mat1,mat2):
    matmult=[]
    for i in range(len(mat1)):
        linha=[]
        for j in range(len(mat1[i])):
            elemento=0
            for k in range(len(mat1[i])):
                elemento=elemento+mat1[i][k]*mat2[k][j]
            linha.append(elemento)
        matmult.append(linha)
    return matmult

print('Digite um número para escolher a operação correspondente:')
try:
    escolha=int(input())
except:
    print('Número inválido. Tente de novo.')
    escolha=int(input())    
print('1 - Soma de duas matrizes mxn')
print('2 - Multiplicação de duas matrizes mxp e pxn')
if escolha==1:
    m=int(input('Digite o número de linhas das matrizes: '))
    n=int(input('Digite o número de colunas das matrizes: '))
    mat1=[]
    print('Começe com a primeira matriz. Digite os elementos, 1 a 1, de cada coluna em cada linha, finalizando com Enter.')
    for i in range(m):
        linha=[]
        for j in range(n):
    escolha=int(input())
except:
    print('Número inválido. Tente de novo')
    escolha=int(input())
            elemento=float(input())
            linha.append(elemento)
        mat1.append(linha)
    mat2=[]
    print('Agora a segunda matriz. Faça o mesmo processo, 1 elemento a 1.')
    for i in range(m):
        linha=[]
        for j in range(n):
            elemento=float(input())
            linha.append(elemento)
        mat2.append(linha)
    print('A matriz 1 é: ', mat1)
    print('A matriz 2 é: ', mat2)
    matsoma=soma(mat1,mat2)
    print('A soma da matriz 1 com a matriz 2 é: ', matsoma)
elif escolha==2:
    m=int(input('Digite o número de linhas da primeira matriz: '))
    p=int(input('Digite o número de colunas da primeira matriz. Note que para a multiplicação ser válida, o número inserido agora deve ser igual ao número de linhas da segunda matriz: '))
    n=int(input('Digite o número de colunas da segunda matriz: '))
    mat1=[]
    print('Começe com a primeira matriz. Digite os elementos, 1 a 1, de cada coluna em cada linha, finalizando com Enter.')
    for i in range(m):
        linha=[]
        for j in range(p):
            elemento=float(input())
            linha.append(elemento)
        mat1.append(linha)
    mat2=[]
    print('Agora a segunda matriz. Faça o mesmo processo, 1 elemento a 1.')
    for i in range(p):
        linha=[]
        for j in range(n):
            elemento=float(input())
            linha.append(elemento)
        mat2.append(linha)
    print('A matriz 1 é: ', mat1)
    print('A matriz 2 é: ', mat2)
    matmult=mult(mat1,mat2)
    print('A multiplicação da primeira matriz pela segunda é: ', matmult)
else:
    print('Opção inválida!')
