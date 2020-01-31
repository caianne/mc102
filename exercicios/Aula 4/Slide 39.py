#Slide 38 da Aula 4

n1=(input())
n2=(input())
n3=(input())

if n2>n1:
	if n3>=n2:
		print(n3, n2, n1)
	if n2>n3:
		if n3>=n1:
			print(n2, n3, n1)
		if n1>n3:
			print(n2, n1, n3)
if n1==n2:
	if n3>=n2:
		print(n3, n2, n1)
	if n2>n3:
		print(n2, n1, n3)
if n1>n2:
	if n2>=n3:
		print(n1, n2, n3)
	if n3>n2:
		if n3>=n1:
			print(n3, n1, n2)
		if n1>n3:
			print(n1, n3, n2)
	
