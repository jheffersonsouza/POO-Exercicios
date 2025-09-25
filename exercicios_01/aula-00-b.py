def eh_palindromo(number):
    num_str = str(number)
    return num_str == num_str[::-1]


number = int(input("Coloque o numero: "))
if eh_palindromo(number):
    print(f"{number} eh palindromo")
else:
    print(f"{number} n eh palindromo!")
