num1 = int(input("Please enter a single digit number:"))
num2 = 0

if num1 < 0 or num1 >= 10:
    print("Invalid number")
else:
    while num2 <= num1:
        print("Next value is {}".format(num2))
        num2 += 2
