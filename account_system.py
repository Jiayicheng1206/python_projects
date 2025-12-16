import getpass

print("Welcome!")
name = input("Name:")
password = getpass.getpass("Password:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

print("Now please login:")
_name = input("Name:")
_password = getpass.getpass("Password:")
if _name == name and _password == password:
    info = f'''---Info of {name}---
Name: {name}
Password: {password}
Age: {age}
Job: {job}
Salary: {salary}
'''
    print(f"Welcome {name}\n",info)
else:
    print("Your name or password is wrong")