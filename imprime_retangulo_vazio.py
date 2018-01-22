def imprime_retangulo_vazio(x, y):
    l = 1
    a = 1
    while a <= y:
        while l <= x:
            if (a == 1 or a == y) or (l == 1 or l == x):
                print('#', end = "")
                l += 1
            else:
                print(' ', end = "")
                l += 1
        print()
        l = 1
        a += 1
        
def main():
    largura = int(input('Digite a largura: '))
    altura = int(input('Digite a altura: '))
    imprime_retangulo_vazio(largura, altura)
    
main()