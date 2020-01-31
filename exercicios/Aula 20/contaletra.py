# Slide 10 e 15 da Aula 20
import string
def verifica(letra,pontuacao):
    if letra in pontuacao:
        return 2
    if letra==' ':
        return 2
    return 3
stri=input()
stri=stri.lower()
cont={}
pontuacao=string.punctuation
for i in range(len(stri)):
    if verifica(stri[i],pontuacao)==3:
        if stri[i] in cont:
            cont[stri[i]]=cont[stri[i]]+1
        else:
            cont[stri[i]]=1
print(cont)
letrafreq=''
for i in cont:
    if letrafreq=='':
        letrafreq=i
    if cont[i]>cont[letrafreq]:
        letrafreq=i
print(letrafreq)