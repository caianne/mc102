import string

longo=input()
longo=longo.lower()
pontuacao=string.punctuation
longo=list(longo)
for i in longo:
    if i in pontuacao:
        longo.remove(i)
        print(longo)
print(longo)
'''
''.join(longo)
longo=longo.split()
contagem={}
for palavra in longo:
    if palavra in contagem:
        contagem[palavra]=contagem[palavra]+1
    else:
        contagem[palavra]=1
print(contagem)'''