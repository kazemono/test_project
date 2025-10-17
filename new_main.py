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
# New operation
elif  operation == "//":
    print(n1 // n2)
# New operation
elif operation == "%":
    print(n1 % n2)
elif operation == "/help":
    print("Извените, в данный момент, я не могу вам помочь")
#Remember guys it!!
else:
    print(n1 / n2)

print("Рад, что воспользовались нашим калькулятором!")
print("Надеюсь вы были удовлетворенными нашей программой!")