a=int(input("Digite um Valor:"))
b=int(input("Digite um Valor:"))
c=int(input("Digite um Valor:"))
if a<b and a<c and c>b:
    print(c,b,a)
elif a<b and a<c and b>c:
    print(b,c,a)
elif b<a and b<c and c>a:
    print(c,a,b)
elif   b<c and b>a and a>c:
    print(a,c,b)
elif c<a and c<b and b>a:
    print(b,a,c)
elif c<a and c<b and a>b:
    print(a,b,c) 
elif a==b and b==c and c==a:
    print("Digite números diferentes")