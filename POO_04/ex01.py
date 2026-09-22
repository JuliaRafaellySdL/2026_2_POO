x=[40, [10,20,30]]
print(x[1][2])
print("Elementos: ", len(x)) #função
print("Elementos dentro do indice 1:", len(x[1]))

#print(x.len()) se fosse um método 


#print(int("Teste")) #ValueError
#print(x[5]) #IndexError
#print(1/0) #ZeroDivisionError

#raise ValueError() #criar um erro
    #Dentro do int --> raise ValueError

#Métodos mágicos da class int
    #Divisão __truediv__

x=int()
print(x) #0