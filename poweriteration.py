import numpy as np

def normalize(x):
    fac = abs(x).max() # Saca el valor abosluto máximo del Vector Columna 
                        #valor propio dominante, autovalor
    print(' fac ', fac)
    x_n = x /x.max() # se multiplica por la inversa del auntovalor dominante
                       # x.max()
    print(x_n, " xn")
    return fac, x_n

x = np.array([1,1,1])
#x= np.random.rand(3)
a = np.array(G)
print('Eigenvalue:', x)
print('Eigenvector:', a)

margen=0.0000000000000000000001
i=0
#for i in range(20):
while(true):
    x = np.dot(a, x)
    print(i, ' iesima= ', x)
    i=i+1
    lambda_backup=lambda_1
    lambda_1, x = normalize(x)
    if(abs(lambda_backup-lambda_1)<margen):
        break
print('Eigenvalue:', lambda_1)
print('Eigenvector:', x)
