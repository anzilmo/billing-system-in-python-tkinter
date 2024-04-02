#calculator
def add(num1,num2):
  return num1+num2

def sub(num1,num2):
  return num1-num2

def mul(num1,num2):
  return num1*num2

def div(num1,num2):
  return num1/num2
while True:
    
 print('Calculator')
 print('-----------------------------------')
 print("1:Add")
 print("2:Subtract")
 print("3:Maliplication")
 print("4:Divition")
 print("5:Quit")
 option=input("Select your option : 1,2,3,4,5\t:")

 if option == '5':
    print("Exiting programm...!")
    break
 if option in ('1','2','3','4'):
   num1=float(input("Ente your first  number\t:"))
   num2=float(input("Ente your second number\t:"))
   if option == '1':
     print("Result:",add(num1,num2))
   elif option=='2':
     print("Result",sub(num1,num2))
   elif option=='3':
     print("Result",mul(num1,num2))  
   elif option=='4':
     print("Result\t:",div(num1,num2))   
else :
    print("Invelid option not asspeted")     
