value = int(input("Informe um valor qualquer: "))

while (value <= 0): 
    value = int(input("Informe um valor positivo: "))

startInterval = int(input("Informe o ínicio do intervalo: "))
endInterval = int(input("Informe o final do intervalo: "))

while (endInterval <= startInterval): 
    endInterval = int(input("O valor final do intervalo deve ser maior que o valor inicial: "))

index = startInterval
while (index <= endInterval):
    result = value * index
    print(f"{value} X {index} = {result}")
    index = index + 1
