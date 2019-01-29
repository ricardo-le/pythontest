file = open("D://password.txt")
password = file.read()
while 1 == 1:
    print("Enter your password")
    typepassword = input()
    if password == typepassword:
        print('yes')
        break
    else:
        print('no')
