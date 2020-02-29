# Considerando a queda de uma bomba com velocidade constante em y, calcular a diferença entre o tempo de queda em y e o tempo para se chegar num ponto a uma distância d do local de queda inicial, dada uma velocidade constante em x.
# Programa para calcular o tempo de ação (t_acao), dadas 4 variáveis: altura inicial (h), velocidade de queda constante na vertical (vb), distância de alcançe desejado (d) e força de empuxo na direção horizontal (T). Baseado nas condições do problema, a velocidade horizontal é, em módulo, igual a T.
# Entradas (em cada linha): h, vb, d, T.
# Saída: t_acao
# Nome: Anne Feng Cai; RA: 261026

h=float(input())
vb=float(input())
d=float(input())
T=float(input())

t_acao=(h/vb)-(d/T)
print('%.3f' %t_acao)

