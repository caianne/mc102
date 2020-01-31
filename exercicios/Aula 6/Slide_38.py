#Slide 38 da Aula 06

print('Olá! Digite o número correspondente ao prato que você quer saber mais sobre:')
print('1 - Feijoada carioca')
print('2 - Bife à milanesa')
print('3 - Macarronada francesa')
print('4 - Strogonoff de frango')
print('5 - Sair do programa')

opcao=int(input())

if opcao==1:
    print('1 - Feijoada carioca: \n    Ingredientes: Feijão preto e carne de porco')
elif opcao==2:
    print('2 - Bife à milanesa: \n    Ingredientes: Bife à milanesa temperado')
elif opcao==3:
    print('3 - Macarronada francesa: \n    Ingredientes: Macarrão do tipo Conchiglione com molho branco, frango em pedaços, azeitona e manjericão')
elif opcao==4:
    print('4 - Strogonoff de frango: \n    Ingredientes: Frango em pedaços, leite, requeijão, alho e cebola')
while opcao==5:
    print('Saindo do programa...')
    break
