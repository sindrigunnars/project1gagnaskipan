
def modulus(a, b):
    if a < b:
        return a
    if a == b:
        return 0
    return modulus(a-b, b)
    
def duplicate(lis, value):
    if lis == []:
        return False
    if lis[0] == value:
        return True
    return duplicate(lis[1:], value)

def how_many(lis1, lis2):
    if lis1 == []:
        return 0
    if duplicate(lis2, lis1[0]):
        return 1 + how_many(lis1[1:], lis2)
    return how_many(lis1[1:], lis2)


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print(f'The modulus of {str(num1) } and {str(num2)} is {str(modulus(num1, num2))} \t{modulus(num1, num2) == num1%num2}')

def test_how_many(lis1, lis2):
    print(f'{str(how_many(lis1, lis2))} of the items in {str(lis1)} are also in {str(lis2)} \t{len([i for i in lis1 if i in lis2]) == how_many(lis1, lis2)}')

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])


if __name__ == "__main__":
    run_recursion_program()