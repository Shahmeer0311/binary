a = int(input("Enter a decimal number"))
x = bin(a)[2:]
print(x)


def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ''
    while n  > 0:
        binary = str(n % 2 ) + binary
        n = n // 2 
    return binary 
b = int(input("Enter a decimal number"))
c = decimal_to_binary(b)
print(c)