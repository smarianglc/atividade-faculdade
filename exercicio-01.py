#Escreva uma função chamada nested_sum que receba uma lista de listas de
#números inteiros e adicione os elementos de todas as listas aninhadas. Por
#exemplo:

def nested_sum(t):
   #calcuar o total dos numeros em uma lista de listas

    total = 0
    for nested in t:
        total += sum(nested)
    return total

if __name__ == "__main__":
    t= [[1,2],[3],[4, 5, 6]]
    print(nested_sum(t))