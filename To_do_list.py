#to do list
todo_list=[]
def addlist():
  item=input("Enter TODAY list")
  todo_list.append(item)
  print(f"(item)add to list")
def displylist():
  print("----------------------")
  print("To do list")
  print("----------------------")
for index,item in enumerate(todo_list,start=1):
  print(f"{index}-{item}")  
def removlist():
  displylist()
  index=int(input("Enter your Remove item"))-1
  if 0<=index<len(todo_list):
    remov_item=todo_list.pop(index)
    print(f"{remov_item} Removed youre item")
  else:
    print("Invalid input")
while True:
  print("To do list")
  print("-----------------------")
  print("1\tadd to list")
  print("2\tDispaly list")
  print("3\tRemove")
  print("4\t Exit")

  option =input("Select your option \t:")
  if  option == '1':
    print("add")
  elif option=='2':
    print("Disply list")
  elif option=='3':
    print("Remove")
  elif option=='4':
    print("Exit")
    break
else :
  print("Invalid option")   


 


