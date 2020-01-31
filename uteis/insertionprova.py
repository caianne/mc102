#código da prova
for i in range(len(v)-1):
        if v[i]>v[i+1]:
                aux=v[i+1]
                v[i+1]=v[i]
                j=i-1
                while (j>=0):
                    if v[j]>aux: #a condição ser colocada aqui fazia com que a ordenação ficassse se sobrepondo
                        v[j+1]=v[j]
                        j=j-1 #esse erro de identação dava looping infinito no while
                v[j+1]=aux
                
#código correto
for i in range(len(v)-1):
        if v[i]>v[i+1]:
                aux=v[i+1]
                v[i+1]=v[i]
                j=i-1
                print(v)
                while (j>=0 and v[j]>aux):
                    v[j+1]=v[j]
                    j=j-1
                v[j+1]=aux
