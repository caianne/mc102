'''
Nome: Anne Feng Cai; RA:261026
Descrição: Programa de análise de substrings em uma string
Entrada: Uma string criptografada
Saída: Direções de bússola e ângulos de elevação

def minmai(str): #ou usar string.lower()
    str=str.replace('A','a')
    str=str.replace('B','b')
    str=str.replace('C','c')
    str=str.replace('D','d')
    str=str.replace('E','e')
    str=str.replace('F','f')
    str=str.replace('G','g')
    str=str.replace('H','h')
    str=str.replace('I','i')
    str=str.replace('J','j')
    str=str.replace('K','k')
    str=str.replace('L','l')
    str=str.replace('M','m')
    str=str.replace('N','n')
    str=str.replace('O','o')
    str=str.replace('P','p')
    str=str.replace('Q','q')
    str=str.replace('R','r')
    str=str.replace('S','s')
    str=str.replace('T','t')
    str=str.replace('U','u')
    str=str.replace('V','v')
    str=str.replace('W','w')
    str=str.replace('X','x')
    str=str.replace('Y','y')
    str=str.replace('Z','z')
    return str'''
coord=[]; ang=[]
pub=str(input())
pub=pub.lower()
pub=pub.split() #lista com as strings separadas
plan=['mercurio','venus','terra','marte','jupiter','saturno','urano','netuno']
dire=['N','NE','L','SE','S','SO','O','NO']
cor=['verde','amarelo','vermelho']
elev=['30','45','60']
for i in range(len(pub)):
    for j in range(len(plan)):
        if pub[i]==plan[j]:
            coord.append(dire[j])
            x=i+1
            break
    if pub[i]==plan[j]:
        for k in range(x,len(pub)): #para procurar a string da cor só depois do índice do planeta
            for l in range(len(cor)):
                if pub[k]==cor[l]:
                    ang.append(elev[l])
                    i=k #para continuar a busca pelo próximo planeta só depois do índice da cor
                    break
            if pub[k]==cor[l]:
                break
for k in range(len(coord)):
    print(coord[k]+' - '+ang[k])
