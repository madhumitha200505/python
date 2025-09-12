def series_sum(n):
    total = 0
    for i in range(1, n + 1):
        term = ((-1)**(i+1)) * (i / math.factorial(i))
        total += term
    return total

n = int(input("Enter the number of terms: "))
result = series_sum(n)
print(f"The sum of the series for {n} terms is {result}")