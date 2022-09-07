#addition function
def add(n1,n2):
    return n1+n2

#subtraction function
def sub(n1,n2):
    return n1-n2

#multiplication function
def mul(n1,n2):
    return n1*n2

#division function 
def divide(n1,n2):
    return n1/n2

#dictionary for operation
#here we assigned key and in place of value we called function itself 
operations={
    '+':add,
    '-':sub,
    '*':mul,
    '/':divide
}

def calculator():
    num1=float(input('whats your first no.- '))
    for symbol in operations:
        print(symbol)
    a=1
    while a>0:
        choose=input('enter the symbol of operation you want to perform- ')
        num2=float(input('whats your second no- '))
        calculation=operations[choose]
        final=calculation(num1,num2)
        print(f'{num1}{choose}{num2}={final}')
        ask=input('do you want to continue than type "y" and to exit calculation type "n" :--> ').lower()
        if ask=='y':
            num1=final
        else:
            a=0
            calculator()

calculator()

        