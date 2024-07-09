from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

        write_key()

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt 
'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


# master_pwd = input("What is the master password? ")
key = load_key() # + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ",user,", Password: ",fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view | add | q to quit) ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue