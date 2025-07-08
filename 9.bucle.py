import time

continua = True

while continua:
    tastat = input("Introduceti cevaa...")
    if not tastat:
        continua = False
    if tastat == "exit":
        break    
else:
    print("Acesta este la final")

print("Acest print este dupa while")