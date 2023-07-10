#How to get the email ids from json or dictionary
contacts_email = {
    "number":3,
    "students":[
        {"name":"guru", "email":"sbalagur@ford.com"},
         {"name":"sunil", "email":"ss6@ford.com"},
         {"name":"ravi", "email":"travicha@ford.com"}
    ]
}
print("Below are the email ids of the students")
#for student in (contacts_email["students"]):
for student in (contacts_email.get("students")):
  print(student['email'])

menu = {
    "breakfast":["idly","Dosa","Pongal"],
    "Lunch":["Rice","Sambar","Appalam","Rasam","curd","pickle"],
    "Dinner":["Chappathi","Gravy","Salad"]
}
print("Today's menu details are below :")
for name,menus in menu.items():
    print(name,":",menus)

print("Different try")
print(menu.get("Lunch")[1])
