year_initial = int(input("ingrese el año inicial: "))
year_final = int(input("ingrese el año final: "))

for i in range(year_initial, year_final):
    if ((i%4==0) and (i%100!=0))|(i%400==0)and (i%10==0):
        print(i)