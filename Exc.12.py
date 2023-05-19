prijem = int(input('Zadaj prijem:\n'))
if prijem <= 10000:
    tax = 0
elif (prijem > 10000) and (prijem <= 20000):
    tax = 10000*0 + (prijem - 10000)*0.1
else:
    tax = 10000*0 + 10000*0.1 + (prijem - 20000)*0.2

print(tax)

