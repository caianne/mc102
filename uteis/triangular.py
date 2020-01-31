n=int(input())
m = ((-1+(8*n+1)**(1/2)))/2 #só vamos considerar m positivo, então somente a solução com +raiz(delta) serve
if m%1==0:  #compara com zero o valor obtido como resto da divisão inteira; se for 0 quer dizer que o número é inteiro, e se é inteiro, então existe um m tal que a soma de 1 até m resulte em n
    print('número triangular')
else:
    print('número não triangular')
