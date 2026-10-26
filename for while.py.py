
#1. Print 1 to 10
#For Loop:
for i in range(1, 11):
    print(i)

#While Loop:
i = 1
while i <= 10:
    print(i)
    i += 1


#2. Print 10 to 1
#For Loop:
for i in range(10, 0, -1):
    print(i)

#While Loop:
i = 10
while i >= 1:
    print(i)
    i -= 1


#3. Print even numbers from 1 to 10
#For Loop:
for i in range(2, 11, 2):
    print(i)

#While Loop:
i = 2
while i <= 10:
    print(i)
    i += 2


#4. Print odd numbers from 1 to 10
#For Loop:
for i in range(1, 11, 2):
    print(i)

#While Loop:
i = 1
while i <= 10:
    print(i)
    i += 2


#5. Sum of numbers from 1 to 10
#For Loop:
s = 0
for i in range(1, 11):
    s += i
print(s)

#While Loop:
i = 1
s = 0
while i <= 10:
    s += i
    i += 1
print(s)


#6. Print the table of 2
#For Loop:
for i in range(1, 11):
    print(2 * i)

#While Loop:
i = 1
while i <= 10:
    print(2 * i)
    i += 1


#7. Print the table of any number
#For Loop:
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#While Loop:
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


#8. Print Hello 5 times
#For Loop:
for i in range(5):
    print("Hello")

#While Loop:
i = 1
while i <= 5:
    print("Hello")
    i += 1


#9. Print squares of 1 to 5
#For Loop:
for i in range(1, 6):
    print(i * i)

#While Loop:
i = 1
while i <= 5:
    print(i * i)
    i += 1


#10. Print cubes of 1 to 5
#For Loop:
for i in range(1, 6):
    print(i ** 3)

#While Loop:
i = 1
while i <= 5:
    print(i ** 3)
    i += 1


#11. Sum of even numbers from 1 to 10
#For Loop:
s = 0
for i in range(2, 11, 2):
    s += i
print(s)

#While Loop:
i = 2
s = 0
while i <= 10:
    s += i
    i += 2
print(s)


#12. Sum of odd numbers from 1 to 10
#For Loop:
s = 0
for i in range(1, 11, 2):
    s += i
print(s)

#While Loop:
i = 1
s = 0
while i <= 10:
    s += i
    i += 2
print(s)


#13. Find factorial of a number
#For Loop:
n = int(input("Enter number: "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f)

#While Loop:
n = int(input("Enter number: "))
i = 1
f = 1
while i <= n:
    f *= i
    i += 1
print(f)


#14. Print multiples of 5 up to 50
#For Loop:
for i in range(5, 51, 5):
    print(i)

#While Loop:
i = 5
while i <= 50:
    print(i)
    i += 5


#15. Print multiples of 10 up to 100
#For Loop:
for i in range(10, 101, 10):
    print(i)

#While Loop:
i = 10
while i <= 100:
    print(i)
    i += 10


#16. Print each character of a string
#For Loop:
s = "Python"
for ch in s:
    print(ch)

#While Loop:
s = "Python"
i = 0
while i < len(s):
    print(s[i])
    i += 1


#17. Print all items in a list
#For Loop:
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

#While Loop:
a = [10, 20, 30, 40, 50]
i = 0
while i < len(a):
    print(a[i])
    i += 1


#18. Find the sum of list elements
#For Loop:
a = [10, 20, 30, 40, 50]
s = 0
for i in a:
    s += i
print(s)

#While Loop:
a = [10, 20, 30, 40, 50]
s = 0
i = 0
while i < len(a):
    s += a[i]
    i += 1
print(s)


#19. Count numbers from 1 to 5
#For Loop:
count = 0
for i in range(1, 6):
    count += 1
print(count)

#While Loop:
i = 1
count = 0
while i <= 5:
    count += 1
    i += 1
print(count)


#20. Print numbers from 1 to 50
#For Loop:
for i in range(1, 51):
    print(i)

#While Loop:
i = 1
while i <= 50:
    print(i)
    i += 1


#21. Find the sum of numbers from 1 to 5
#For Loop:
s = 0
for i in range(1, 6):
    s += i
print(s)

#While Loop:
i = 1
s = 0
while i <= 5:
    s += i
    i += 1
print(s)


#22. Print numbers divisible by 3 from 1 to 30
#For Loop:
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

#While Loop:
i = 1
while i <= 30:
    if i % 3 == 0:
        print(i)
    i += 1


#23. Find the average of numbers from 1 to 10
#For Loop:
s = 0
for i in range(1, 11):
    s += i
print(s / 10)

#While Loop:
i = 1
s = 0
while i <= 10:
    s += i
    i += 1
print(s / 10)


#24. Print a star pattern vertically
#For Loop:
for i in range(5):
    print("*")

#While Loop:
i = 1
while i <= 5:
    print("*")
    i += 1


#25. Print a star triangle
#For Loop:
for i in range(1, 6):
    print("*" * i)

#While Loop:
i = 1
while i <= 5:
    print("*" * i)
    i += 1
