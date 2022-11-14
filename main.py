def main():

    import math

    print('Número: ')
    num=input()
    print('Decimales a mostrar')
    deci=int(input())
    
   
   
    varphi= float(num)*((1+math.sqrt(5))/2)
    round(varphi, 2)
    
    print(round(varphi, deci))

if __name__ == '__main__':
    main()
