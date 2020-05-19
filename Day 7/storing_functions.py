def addition(a,b,c):
    val=a+b+c
    return val

def sub(a,b):
    val1=a-b

def make_pizza(size, *toppings):
    print(f'the pizza size of {size}-inch and client requested following toppings: ')
    for item in toppings:
        print(item)

def modulus(a):
    v2=a%2
    if v2==0:
        print(f'The number {a} is even number.')
    else:
        print(f'The number {a} is odd number.')