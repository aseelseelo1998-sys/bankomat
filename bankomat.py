
konton = {}
with open ("bankomat.txt","r") as file:
    for rad in file:
        konto, saldo =rad.strip().split(",")
        konton[konto] = float(saldo)
print(konton)
