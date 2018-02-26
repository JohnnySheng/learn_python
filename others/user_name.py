# names = ['admin', 'Johnny','Mia', 'Tomas','Zipplin']
names = []
if len(names) == 0:
    print("We need to find some users")
print("test")
for name in names:
    if 'admin' == name:
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ", thank you for logging in again!!!")