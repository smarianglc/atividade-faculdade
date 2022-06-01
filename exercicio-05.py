#Escreva uma função chamada is_sorted que tome uma lista 
#como parâmetro e retorne True se a lista estiver classificada em ordem ascendente, 
#e False se não for o caso.

def is_sorted(t):
    return t == sorted(t)
    
if __name__ == "__main__":
    t = [1, 2, 3]
    print(is_sorted(t))
    t = ['b','a']
    print(is_sorted(t))
