def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = check_odd_even(num)

print(f"The number {num} is {result}.")