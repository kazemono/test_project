n1 = int(input())
operation = input()
n2 = int(input())

if operation == "+":
    print(n1 + n2)
elif operation == "-":
    print(n1 - n2)
elif operation == "*":
    print(n1 * n2)
# New Operation
elif operation == "**":
    print(n1 ** n2)
else:
    print(n1 / n2)