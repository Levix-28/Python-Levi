a=int(input("Digite as notas:"))
b=int(input("Digite as notas:"))
c=((a+b)/2)
if c>=7 and c<=9:
    print("Aprovado")
elif c<7:
    print("Reprovado")
elif c==10:
    print("Aprovação com distinção")