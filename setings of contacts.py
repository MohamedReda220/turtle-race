contacts={}

while True:
 print("1-add a contact\n2-view contact\n3-Edit a contact \n4- exit  ")
 user_choise=int(input(" please chose a num 1_4::"))
 if user_choise==1:
  contact_id=int(input(" enter contact ID :"))
  contact_name=input("enter contact s name :")
  contact_num=int(input("enter a contact number:"))
  contacts["ID"]=contact_id
  contacts["name"]=contact_name
  contacts["number"]=contact_num
  print("the contact was added sucsesfuly")
  print("____________________________________________________")
 elif user_choise==2:
  print(contacts)
  print("____________________________________________________")

 elif user_choise==3:
  contact_id=int(input(" enter a new contact ID :"))
  contact_name=input("enter a new contact  name :")
  contact_num=int(input("enter a new contact number:"))
  contacts["ID"]=contact_id
  contacts["name"]=contact_name
  contacts["number"]=contact_num
  print("the contac had changed sucsesfuly")
  print("____________________________________________________")

 else:
   print("the program has ended__")
   break