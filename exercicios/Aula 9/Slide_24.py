#Slide 24 da Aula 09

for n1 in range (2,61,2):
    for n2 in range (1,61,2):
        for n3 in range (n1+2,61,2):
            for n4 in range (n2+2,61,2):
                for n5 in range (n3+2,61,2):
                    for n6 in range (n4+2,61,2):
                        print(n1,n2,n3,n4,n5,n6)
