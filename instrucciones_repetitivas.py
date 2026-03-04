capital= float(input("Digite el capital: "))
meses = 0
dinero = capital
while dinero < capital * 2:
    dinero = dinero + dinero * 0.05
    meses = meses + 1

print("El capital se duplica en" , meses, "meses")
