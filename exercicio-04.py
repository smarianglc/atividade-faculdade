#Escreva uma função chamada chop que tome uma lista alterando-a 
#para remover o primeiro e o último elementos, e retorne None. 

def chop(t):
    del t[0] 
    del t[-1]

if __name__ == "__main__":
    t = [1, 2, 3, 4]
    chop(t)
    print(t)