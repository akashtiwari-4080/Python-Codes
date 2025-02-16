
#first program
num=[12,7,9,15,22,30,5]
for num in num:
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
#second q
age=[12,7,9,14,15,18,22,30,5]
for i in age:
    if i<=12:
        print("you are child ")
    elif i>12 and i<=19:
        print("you are a teenager")
    else:
        print("you are adult")

#third question
list1=[0,1,2,3,4,5,6,7,-1]
for i in list1:
    if i<0:
        print("negative")
    elif i==0:
        print("its zerooo")
    else:
        print("postive")
#fourth
percantage=[50,45,48,95,75,76,45]
for i in percantage:
    if i>=50:
        print("You are passed with good grades")
    else:
        print("you fail the exams.....oops try again")
#fifth
list=[14,15,16,-17,-18,14]
for i in list:
    if i<0:
        print(f"first negative number:{num}")
        break
    elif i==0:
        continue
    else:
        print("there is no negativity")


#q9
s="pythonforloops"
for i in s:
    print(s[::-1])







#q10
for i in range(1,6):
    for j in range(1,11):
        print(i*j)

#q11
num = 12345
sum_of_digits = 0


for digit in str(num):
    sum_of_digits += int(digit)

print("Sum of digits:", sum_of_digits)

#q12
# Initialize the first two Fibonacci numbers
a, b = 0, 1

#q13
# Loop to generate the next 8 Fibonacci numbers
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b  # Update the values of a and b to the next numbers in the series

#q
n = 5
factorial = 1


for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is", factorial)


#q14
for i in range(1,11):
    if i%4==0:
        continue
    elif i>7:
        break
    else:
        print(i)
