#Nome: Anne Feng Cai;RA: 261026
#Descrição: É um programa para calcular o futuro poder de combate (PCf) de monstros baseado em estatísticas anteriores.
#Entrada: A entrada pode ser divida em 4 partes. (1) Número de monstros a serem adicionados no banco de dados; (2) Banco de dados com ID, PCa e PCf; (3) Consulta ao banco de dados com ID e PCa; (4) Encerramento da consulta com 0 0.
#Saída: PCf das respectivas consultas.

numevol=int(input()) #número de evoluções de monstros
monstroslidos=0
listaID = [0 for i in range(400)] #colocar 400 zeros vai do ID[1] até ID[399]
listaMultiplicador=[0 for i in range(400)] #mas no testador aberto, dá para colocar até 345, já fechado não sei
while monstroslidos<numevol: #carregando a base de dados
    bruto = input() #lê a linha com espaços e os 3 tipos de dados
    bruto = [int(i) for i in bruto.split()] #tira os espaços e deixa uma lista com 3 coisas inteiras
    listaID[bruto[0]] = listaID[bruto[0]]+1 #faz a contagem de monstros por espécie, que são achadas pelo índice
    listaMultiplicador[bruto[0]]=listaMultiplicador[bruto[0]] + bruto[2]/bruto[1]
    monstroslidos=monstroslidos+1
consulta = input()
consulta = [int(i) for i in consulta.split()]
while consulta[0]!=0:
    saida=consulta[1]*listaMultiplicador[consulta[0]]/listaID[consulta[0]]
    if saida-saida//1==0:
        print(int(saida))
    else:
        print(int(saida+1))
    consulta = input()
    consulta = [int(i) for i in consulta.split()]
