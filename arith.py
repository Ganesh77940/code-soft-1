def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator():
    print("select the operation:\n1.add\n2.sub\n3.mul\n4.div")
    operation=input("enter your choice(1,2,3,4):")
    if operation in['1','2','3','4']:
        num1=input("enter first number:")
        num2=input("enter second number:")
    if operation=='1':
        print(f"The result is:{add(num1,num2)}")    
    elif operation=='2':
        print(f"The result is:{sub(num1,num2)}")
    elif operation=='3':
        print(f"The result is:{mul(num1,num2)}") 
    elif operation=='4':
        print(f"The result is:{div(num1,num2)}")
    else:
        print("invalid operation choosen")
if __name__=="__main__":               
    calculator()               
