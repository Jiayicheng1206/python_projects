users = {}

with open("users.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
with open("locked.txt", "r", encoding="utf-8") as f:
    locked_users = f.read().splitlines()

for line in lines:
    if not line.strip(): #strip()可以去掉变量中两头的空格、换行等无效空白字符
        continue        #if not xxx: xxx如果为false才进入，字符串如果为空也算一种false
    username, password = line.split(",",1) #最多分割一次
    users[username] = password

while True:
    input_username = input("your username: ")

    if input_username in locked_users:
        print(f"user {input_username} is locked")
        continue

    elif input_username in users:
        print(f"user {input_username} exists")

        for attempts in range(1,4):
            input_password = input("your password:")
            if input_password == users[input_username]:
                print(f"login success! welcome {input_username}")
                break
            else: #输错
                print("wrong password, try again")
        else: #输错3次
            if input_username not in locked_users:
                with open("locked.txt", "a+", encoding="utf-8") as f:
                    f.write(input_username + "\n")
                    f.seek(0)
                    locked_users = f.read().splitlines()
            print(f"you have already tried {attempts} times, your account is locked now")
            continue

    else:
        print(f"user {input_username} not found")
