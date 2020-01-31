#Slide 19 da Aula 05

print('Programa para calcular o valor da comissão, dada o valor da transação.')
transação=float(input('Informe o valor da transação: R$ '))
if (transação<=2500.00):
    comissão=30+0.017*transação
    if (comissão>39.00):
        print('O valor da comissão é: R$ %.2f' %comissão)
    else:
        print('O valor da comissão é: R$ 39.00')
elif (transação>2500.00) and (transação<=6250.00):
    print('O valor da comissão é: R$ %.2f' %(56+0.0066*transação))
elif (transação>6250.00) and (transação<=20000.00):
    print('O valor da comissão é: R$ %.2f' %(76+0.0034*transação))
elif (transação>20000.00) and (transação<=50000.00):
    print('O valor da comissão é: R$ %.2f' %(100+0.0022*transação))
elif (transação>50000.00) and (transação<=500000.00):
    print('O valor da comissão é: R$ %.2f' %(155+0.0011*transação))
elif (transação>500000.00):
    print('O valor da comissão é: R$ %.2f' %(255+0.0009*transação))
