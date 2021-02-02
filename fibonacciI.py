from fibonacciG import fibogenerator

limit = int(input("Enter a number to limit the sequence to."))
x = fibogenerator(limit)
print(x.__next__())
print("\nFibonacci Sequence")
for i in fibogenerator(limit):
    print(i)