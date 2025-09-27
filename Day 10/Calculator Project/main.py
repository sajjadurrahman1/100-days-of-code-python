import art

"""add"""
def add(n1, n2):
    return n1 + n2

"""subtract function"""
def sub(n1, n2):
    return n1 - n2

"""multiply"""
def multiply(n1, n2):
    return n1 * n2

"""division"""
def division(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":division
}
#print(operations["*"](4,8))
def calculator():
    print(art.logo)
    should_continue=True
    n1= float(input("what is your first number\n"))

    while should_continue:

     for symbol in operations:
        print(symbol)
     operation_symbol= input("pick an operation:")

     n2= float(input("enter the second number\n"))
     result= operations[operation_symbol](n1,n2)

     print(f"{n1} {operation_symbol} {n2}: {result}")

     choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
     if choice == "y":
         n1=result

     else:
         should_continue= False
         print("\n" *50)
         calculator()
calculator()